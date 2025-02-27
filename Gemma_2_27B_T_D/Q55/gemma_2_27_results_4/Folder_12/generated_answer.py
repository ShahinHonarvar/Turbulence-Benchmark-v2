def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if functools.reduce(lambda x, y: x * y, nums[i:j], 1) == -18:
                result.append(nums[i:j])
    return result