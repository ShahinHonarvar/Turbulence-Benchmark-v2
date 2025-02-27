def lists_with_product_equal_n(nums):
    n = len(nums)
    cir_nums = nums * 2
    res = []
    for i in range(n):
        for j in range(i + 1, i + n):
            if j - i > n // 2:
                break
            prod = 1
            for k in range(i, j + 1):
                prod *= cir_nums[k]
            if prod == 57:
                res.append(cir_nums[i:j + 1])
    return res