def lists_with_product_equal_n(lst):
    lst = lst + lst[0]
    res = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == 29:
                res.append(lst[i:j + 1])
    return res