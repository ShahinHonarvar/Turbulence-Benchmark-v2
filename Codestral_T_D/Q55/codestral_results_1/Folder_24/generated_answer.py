def lists_with_product_equal_n(lst):
    n = len(lst)
    res = []
    for i in range(n):
        prod = 1
        for j in range(i, n + i):
            prod *= lst[j % n]
            if prod == -89:
                res.append(lst[i:j % n + 1])
    return res