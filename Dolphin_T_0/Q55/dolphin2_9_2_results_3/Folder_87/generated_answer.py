def lists_with_product_equal_n(lst):
    if not lst:
        return []
    l = len(lst)
    res = []
    for i in range(l):
        for j in range(i + 1, l + 1):
            m = 1
            for k in range(i, j):
                m *= lst[k]
            if m == 27:
                res.append(lst[i:j])
    return res