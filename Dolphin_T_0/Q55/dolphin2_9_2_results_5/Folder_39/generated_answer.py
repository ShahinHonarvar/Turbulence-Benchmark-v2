def lists_with_product_equal_n(lst):
    res = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= lst[j]
            if product == -46:
                res.append(lst[i:j + 1])
            if product > -46:
                break
    return res