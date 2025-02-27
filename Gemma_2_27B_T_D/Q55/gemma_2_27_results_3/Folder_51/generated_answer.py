def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + i + 1):
            if (product := reduce(lambda x, y: x * y, nums[i:j])) == -44:
                result.append(nums[i:j])
    return result