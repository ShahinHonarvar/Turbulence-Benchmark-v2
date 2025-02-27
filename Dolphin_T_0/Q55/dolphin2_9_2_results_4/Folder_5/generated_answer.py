def lists_with_product_equal_n(lst, n):
    if not lst or len(lst) == 1:
        return []
    lst = lst + lst[:-1]
    res = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            product = 1
            for k in range(i, j + 1):
                product *= lst[k]
            if product == n:
                res.append(lst[i:j + 1])
    return res