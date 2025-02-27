def lists_with_product_equal_n(lst):
    lst = lst + lst
    res = []
    n = len(lst)
    product = 1
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst[j % n]
            if product == 74:
                res.append(lst[j % n - i + 1:j % n + 1])
    return res