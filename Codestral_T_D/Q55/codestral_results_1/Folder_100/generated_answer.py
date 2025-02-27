def lists_with_product_equal_n(lst):
    l = len(lst)
    lst += lst
    res = []
    for i in range(l):
        for j in range(i + 1, i + l):
            if j - i > l // 2:
                break
            prod = 1
            for k in range(i, j):
                prod *= lst[k]
            if prod == 48:
                res.append(lst[i:j])
    return res