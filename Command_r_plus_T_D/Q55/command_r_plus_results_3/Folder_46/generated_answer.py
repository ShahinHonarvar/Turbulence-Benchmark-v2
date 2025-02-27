def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(nums, target, size):
        result = []
        n = len(nums)
        for i in range(n):
            for j in range(i, min(i + size, n)):
                if i <= j < n and prod(nums[i:j + 1]) == target:
                    result.append(nums[i:j + 1])
        return result

    def prod(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    size = len(circular_list)
    result = []
    for i in range(1, size + 1):
        result.extend(find_subarrays(circular_list, 53, i))
    return result