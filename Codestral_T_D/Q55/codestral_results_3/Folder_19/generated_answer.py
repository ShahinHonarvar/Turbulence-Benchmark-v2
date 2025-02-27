def lists_with_product_equal_n(lst):
    lst *= 2
    n = len(lst)
    result = []
    for i in range(n):
        prod = 1
        sublist = []
        for j in range(i, n):
            prod *= lst[j]
            sublist.append(lst[j])
            if prod == -54:
                result.append(sublist)
    return result