def lists_with_product_equal_n(nums):
    sublists = []
    n = len(nums)
    for i in range(n):
        for j in range(i, n + i):
            product = 1
            sublist = []
            for k in range(i, j % n + 1):
                product *= nums[k % n]
                sublist.append(nums[k % n])
            if product == -690:
                sublists.append(sublist)
    return sublists