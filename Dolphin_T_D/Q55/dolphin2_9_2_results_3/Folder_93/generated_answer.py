def lists_with_product_equal_n(lst):
    res = []
    n = len(lst)
    for i in range(n):
        prod = 1
        for j in range(i, i + n):
            prod *= lst[j % n]
            if prod == -91:
                res.append(lst[i:j + 1])
    return res