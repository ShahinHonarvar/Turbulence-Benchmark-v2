def lists_with_product_equal_n(lst):
    n = len(lst)
    res = []
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst[j % n]
            if product == -779:
                res.append(lst[i:j % n] if j < n else lst[i:] + lst[:j % n])
    return res