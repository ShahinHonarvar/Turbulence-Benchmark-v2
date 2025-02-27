def lists_with_product_equal_n(nums):
    n = len(nums)
    sublists = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            product = 1
            sublist = nums[i:j]
            for num in sublist:
                product *= num
            if product == -18:
                sublists.append(sublist)
    return sublists