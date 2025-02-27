def lists_with_product_equal_n(lst, n=-72):
    if len(lst) == 0:
        return []
    lst = lst + lst[:-1]
    res = []
    for i in range(len(lst) - 1):
        prod = lst[i]
        for j in range(i + 2, len(lst)):
            prod *= lst[j]
            if prod > n:
                break
            if prod == n:
                res.append(lst[i:j + 1])
    return res