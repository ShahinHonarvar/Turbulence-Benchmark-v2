def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def get_product(sublist: list[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product

    def find_subarrays(nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        left, right = ([0] * n, [0] * n)
        left[0] = 1
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1] % 100
        right[n - 1] = 1
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1] % 100
        result = []
        for i in range(n):
            if left[i] == 0:
                continue
            if right[i] * left[i] % 100 == target:
                result.append(nums[i - (n - 1)] if i > 0 else nums[-1])
        return result
    result = []
    for i in range(len(circular_list)):
        sublist = circular_list[i:] + circular_list[:i]
        if get_product(sublist) == 100:
            result.append(sublist)
    subarrays = find_subarrays(circular_list, 100)
    for subarray in subarrays:
        result.append([subarray])
    return result