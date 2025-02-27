def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(nums, target, n):
        result = []
        for i in range(len(nums)):
            for j in range(i, min(i + n, len(nums))):
                if product(nums[i:j + 1]) == target:
                    result.append(nums[i:j + 1])
        return result

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    subarrays = find_subarrays(circular_list, -89, len(circular_list))
    return subarrays