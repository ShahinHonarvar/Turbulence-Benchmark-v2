def lists_with_product_equal_n(lst):
    n = 48
    res = []
    for i in range(len(lst)):
        p = 1
        for j in range(i, len(lst) + i):
            p *= lst[j % len(lst)]
            if p == n:
                res.append(lst[i:j % len(lst) + 1])
            if p > n:
                break
    return res