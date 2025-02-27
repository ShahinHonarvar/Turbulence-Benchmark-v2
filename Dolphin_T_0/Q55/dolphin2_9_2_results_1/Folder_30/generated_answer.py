def lists_with_product_equal_n(lst):
    res = []
    lst_len = len(lst)
    for i in range(lst_len):
        product = 1
        for j in range(lst_len):
            product *= lst[(i + j) % lst_len]
            if product == 99:
                res.append(lst[(i + j - (j - i + 1)) % lst_len:(i + j + 1) % lst_len + 1])
    return res