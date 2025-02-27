def lists_with_product_equal_n(lst):
    n = 99
    res = []
    lst = lst + lst
    for i in range(len(lst)):
        p = 1
        for j in range(i, len(lst)):
            p *= lst[j]
            if p == n:
                res.append(lst[i:j + 1])
            if p > n:
                break
    return res