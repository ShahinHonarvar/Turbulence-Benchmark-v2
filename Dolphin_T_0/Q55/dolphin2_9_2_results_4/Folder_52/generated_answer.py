def lists_with_product_equal_n(nums):
    if not nums:
        return []
    n = len(nums)
    res = []
    product_set = set()
    for i in range(n):
        prod = 1
        for j in range(i, i + n):
            prod *= nums[j % n]
            if prod == 37:
                sublist = nums[i:j + 1]
                circular_sublist = sublist[-1:] + sublist[:-1]
                if list(product_set) == circular_sublist:
                    res.append(sublist)
                else:
                    product_set.add(tuple(sublist))
    return res