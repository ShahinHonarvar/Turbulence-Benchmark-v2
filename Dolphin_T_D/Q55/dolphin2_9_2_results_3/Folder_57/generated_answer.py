def lists_with_product_equal_n(lst):
    n = len(lst)
    res = []
    prod = 1
    for i in range(n):
        if prod == -75:
            res.append(lst[:i + 1])
        for j in range(i, n):
            prod *= lst[j]
            if prod == -75:
                res.append(lst[i:j + 1])
    return res