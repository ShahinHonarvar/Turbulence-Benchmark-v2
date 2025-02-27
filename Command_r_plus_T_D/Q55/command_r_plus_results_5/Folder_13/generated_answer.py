def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(nums, target, size):
        result = []
        for i in range(len(nums)):
            product = 1
            subarray = []
            for j in range(i, min(i + size, len(nums))):
                product *= nums[j]
                subarray.append(nums[j])
                if product == target:
                    result.append(subarray)
        return result
    result = []
    for size in range(1, len(circular_list) + 1):
        result.extend(find_subarrays(circular_list, 54, size))
    return result