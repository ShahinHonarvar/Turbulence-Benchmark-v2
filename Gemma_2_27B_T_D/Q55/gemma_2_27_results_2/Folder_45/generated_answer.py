def lists_with_product_equal_n(nums):
    sublists = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            product = 1
            sublist = nums[i:j + 1]
            for num in sublist:
                product *= num
            if product == -5:
                sublists.append(sublist)
    return sublists