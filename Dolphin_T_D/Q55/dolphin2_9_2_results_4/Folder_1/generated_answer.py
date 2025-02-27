def lists_with_product_equal_n(lst):
    n = len(lst)
    res = []
    product = 1
    for i in range(n):
        product *= lst[i]
        if product == -51:
            res.append(lst[0:i + 1])
            product = 1
    return res