def lists_with_product_equal_n(lst):
    res = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst[j % n]
            if product == 10 and [lst[k % n] for k in range(i, j)] not in res:
                res.append([lst[k % n] for k in range(i, j)])
    return res