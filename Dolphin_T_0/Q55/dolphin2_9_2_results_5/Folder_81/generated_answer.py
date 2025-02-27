def lists_with_product_equal_n(lst):
    res = []
    n = len(lst)
    for i in range(n):
        prod = 1
        for j in range(i, i + n):
            prod *= lst[j % n]
            if prod == -8:
                res.append(lst[i:j % n + 1])
    return res