def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    lst = lst + lst[:2]
    res = []
    for i in range(n + 2):
        product = 1
        for j in range(i, n + i + 1):
            product *= lst[j % n]
            if product == 2:
                res.append(lst[j % n - i:j % n])
    return res