def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i, i + n):
            prod = 1
            sublist = []
            for k in range(i, j + 1):
                prod *= nums[k % n]
                sublist.append(nums[k % n])
                if prod == 40:
                    result.append(sublist)
    return result