def lists_with_product_equal_n(nums):
    n = len(nums)
    nums += nums
    res = []
    for i in range(n):
        prod = 1
        for j in range(i, i + n):
            prod *= nums[j]
            if prod == 27:
                res.append(nums[i:j + 1])
            elif prod > 27:
                break
    return res