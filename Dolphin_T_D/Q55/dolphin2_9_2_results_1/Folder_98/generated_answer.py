def lists_with_product_equal_n(nums):
    res = []
    n = len(nums)
    for i in range(n):
        prod = 1
        for j in range(n):
            prod *= nums[(i + j) % n]
            if prod == -1:
                res.append(nums[i:j + i + 1])
    return res