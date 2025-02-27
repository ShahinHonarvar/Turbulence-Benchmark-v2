def lists_with_product_equal_n(nums):
    sublists = []
    for i in range(len(nums)):
        product = 1
        for j in range(i, len(nums)):
            sublists.append(nums[j])
            product *= nums[j]
            if product == 25:
                if sublists not in sublists:
                    sublists.append(sublists)
            elif product > 25 or (len(sublists) != 1 and len(sublists) > 1 and (sublists[-1] == sublists[-2])):
                sublists.pop()
                product /= nums[j]
    return sublists