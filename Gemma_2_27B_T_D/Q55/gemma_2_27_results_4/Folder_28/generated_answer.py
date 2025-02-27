def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if len(nums[i:j + 1]) > len(nums):
                break
            if 85 == eval('*'.join((str(x) for x in nums[i:j + 1]))):
                res.append(nums[i:j + 1])
    return res