def lists_with_product_equal_n(lst):
    res = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == 8:
                res.append(lst[i:j + 1])
            if product > 8:
                break
    return res