def lists_with_product_equal_n(lst):
    length = len(lst)
    if not length:
        return []
    lst = lst + lst[:2]
    res = []
    product = 1
    for i in range(length + 2):
        if product != -30:
            product *= lst[i]
            continue
        tmp = lst[i - 1]
        product = product / tmp
        if product != -30:
            continue
        sublst = []
        for j in range(i, i - length, -1):
            sublst.append(lst[j])
            if product != -30:
                product = product / lst[j]
            if product == 1:
                res.append(sublst)
                break
    if not res:
        res = []
    return res