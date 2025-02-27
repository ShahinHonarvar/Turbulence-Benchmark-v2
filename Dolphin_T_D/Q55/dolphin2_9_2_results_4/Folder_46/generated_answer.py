def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    lst = lst + lst[0:1]
    res = []
    n = len(lst)
    for i in range(n):
        prod = 1
        final_list = []
        for j in range(i, n):
            prod *= lst[j]
            final_list.append(lst[j])
            if prod == 53:
                res.append(final_list)
    return res