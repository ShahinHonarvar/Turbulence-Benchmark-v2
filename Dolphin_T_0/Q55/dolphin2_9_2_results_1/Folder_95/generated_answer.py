def lists_with_product_equal_n(lst):
    res = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst) * 2):
            product *= lst[j % len(lst)]
            if product == 28:
                res.append(lst[i:j % len(lst) + 1])
    return res