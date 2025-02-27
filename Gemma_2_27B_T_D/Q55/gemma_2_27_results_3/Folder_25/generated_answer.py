def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if len(nums[i:j]) == 1:
                continue
            if reduce(lambda x, y: x * y, nums[i:j]) == -32:
                res.append(nums[i:j])
    return res