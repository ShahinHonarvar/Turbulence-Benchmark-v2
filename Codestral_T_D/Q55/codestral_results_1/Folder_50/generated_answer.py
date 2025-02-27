def lists_with_product_equal_n(lst):
    n = 45
    res = []
    for i in range(len(lst)):
        prod = 1
        for j in range(i, len(lst) + i):
            prod *= lst[j % len(lst)]
            if prod == n:
                res.append(lst[i:j + 1] if i <= j else lst[i:] + lst[:j + 1])
            if prod > n:
                break
    return res