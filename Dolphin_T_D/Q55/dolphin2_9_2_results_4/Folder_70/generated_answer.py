def lists_with_product_equal_n(lst):
    res = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n + 1):
            product = 1
            for k in range(i, j):
                product *= lst[k % n]
            if product == 32:
                res.append(lst[i:j])
    return res