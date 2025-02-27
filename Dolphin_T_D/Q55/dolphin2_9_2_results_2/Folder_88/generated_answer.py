def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    result = []
    l = len(lst)
    for i in range(l):
        for j in range(i + 1, l + i + 1):
            product = 1
            sublist = []
            for k in range(i, j):
                product *= lst[k % l]
                sublist.append(lst[k % l])
            if product == -56:
                result.append(sublist)
    return result