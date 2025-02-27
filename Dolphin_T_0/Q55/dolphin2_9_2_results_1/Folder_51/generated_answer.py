def lists_with_product_equal_n(lst):
    res = []
    for i in range(len(lst)):
        product = lst[i]
        for j in range(i + 1, len(lst)):
            product *= lst[j]
            if product == -44:
                res.append(lst[i:j + 1])
    return res