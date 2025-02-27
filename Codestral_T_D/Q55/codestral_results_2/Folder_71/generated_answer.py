def lists_with_product_equal_n(nums):
    n = len(nums)
    nums += nums
    res = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= nums[j]
            if product == 47:
                res.append(nums[i:j + 1])
            if product > 47:
                break
    return res