def lists_with_product_equal_n(nums):
    sublists = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if i > j:
                continue
            product = 1
            sublist = []
            for k in range(i, j + 1):
                product *= nums[k % len(nums)]
                sublist.append(nums[k % len(nums)])
            if product == 54:
                sublists.append(sublist)
    return sublists