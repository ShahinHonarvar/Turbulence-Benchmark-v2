def lists_with_product_equal_n(nums):
    n = len(nums)
    sublists = []
    for i in range(n):
        for j in range(i, n):
            product = 1
            for k in range(i, j + 1):
                product *= nums[k % n]
            if product == 733:
                sublists.append(nums[i:j + 1])
    return sublists