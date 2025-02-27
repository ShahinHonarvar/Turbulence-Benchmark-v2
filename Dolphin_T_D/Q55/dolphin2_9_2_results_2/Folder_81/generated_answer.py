def lists_with_product_equal_n(lst, n=-8):
    res = []
    lst_length = len(lst)
    for i in range(lst_length):
        product = lst[i]
        if product == n:
            res.append([lst[i]])
        for j in range(i + 1, lst_length + i):
            j_modulo = j % lst_length
            product *= lst[j_modulo]
            if product == n:
                res.append(lst[i:j + 1])
            elif product > n:
                break
    return res