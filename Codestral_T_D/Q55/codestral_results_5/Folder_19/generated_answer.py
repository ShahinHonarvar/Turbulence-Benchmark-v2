def lists_with_product_equal_n(lst):
    n = -54
    res = []
    for i in range(len(lst)):
        prod = 1
        for j in range(i, len(lst)):
            prod *= lst[(j - i) % len(lst)]
            if prod == n:
                res.append(lst[i:j + 1] or lst[i:] + lst[:j - i + 1])
    return res