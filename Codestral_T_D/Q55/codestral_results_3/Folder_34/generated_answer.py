def lists_with_product_equal_n(nums):
    n = len(nums)
    nums = nums + nums
    res = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= nums[j]
            if product == -81:
                res.append(nums[i:j + 1])
    return res