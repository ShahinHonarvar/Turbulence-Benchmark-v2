def lists_with_product_equal_n(nums):
    n = len(nums)
    product = 1
    sublists = []
    for i in range(n):
        product *= nums[i]
    if product != 93:
        return []
    for i in range(n):
        sublist = []
        if nums[i] != 1 and 93 % nums[i] == 0:
            for j in range(i, n):
                sublist.append(nums[j])
                product /= nums[j]
                if product == 1:
                    sublists.append(sublist[:])
                    break
    return sublists