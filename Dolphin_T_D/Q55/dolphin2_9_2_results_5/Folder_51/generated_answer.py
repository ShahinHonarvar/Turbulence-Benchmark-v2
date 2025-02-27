def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    product = -44
    sublists = []
    for i in range(n):
        for j in range(i, n):
            sublist = lst[i:j + 1]
            sublist_product = 1
            for k in sublist:
                sublist_product *= k
            if sublist_product == product:
                sublists.append(sublist)
    return sublists