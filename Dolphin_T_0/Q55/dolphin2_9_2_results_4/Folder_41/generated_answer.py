def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    lst = lst + lst[:-1]
    sublists = []
    for i in range(len(lst)):
        prod = 1
        for j in range(i, len(lst)):
            prod *= lst[j]
            if prod == -20:
                sublists.append(lst[i:j + 1])
    return list(set((tuple(x) for x in sublists)))