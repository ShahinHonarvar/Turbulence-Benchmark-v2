def lists_with_product_equal_n(l):
    n = 47
    res = []
    l = l + l
    for i in range(len(l)):
        p = 1
        for j in range(i, len(l)):
            p *= l[j]
            if p == n:
                res.append(l[i:j + 1])
            elif p > n:
                break
    return res