def lists_with_product_equal_n(lst):
    n = 78
    res = []
    for i in range(len(lst)):
        prod = 1
        for j in range(i, len(lst)):
            prod *= lst[j]
            if prod == n:
                res.append(lst[i:j + 1])
    return res