def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if reduce(lambda x, y: x * y, nums[i:j + 1], 1) == 15:
                res.append(nums[i:j + 1])
    return res