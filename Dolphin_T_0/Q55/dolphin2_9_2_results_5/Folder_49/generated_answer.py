def lists_with_product_equal_n(lst):
    n = len(lst)
    res = []
    for i in range(n):
        product = 1
        sublist = [lst[i]]
        for j in range(i + 1, n):
            product *= lst[j]
            sublist.append(lst[j])
            if product == -61:
                res.append(sublist)
            if product > -61:
                break
        for j in range(i + 1, n):
            product /= lst[i + j]
            sublist.pop(0)
            if product == -61:
                res.append(sublist)
            if product > -61:
                break
            product /= lst[i + j]
    return res