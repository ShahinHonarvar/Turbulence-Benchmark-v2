def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i, n):
            product = 1
            sublist = []
            for k in range(i, j + 1):
                product *= nums[k % n]
                sublist.append(nums[k % n])
            if product == 851:
                result.append(sublist)
    return result