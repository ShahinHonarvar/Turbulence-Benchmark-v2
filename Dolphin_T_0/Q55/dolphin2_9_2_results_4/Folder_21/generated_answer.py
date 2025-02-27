def lists_with_product_equal_n(lst):
    res = []
    n = len(lst)
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i + n):
            product *= lst[j % n]
            sublist.append(lst[j % n])
            if product == 851:
                res.append(sublist)
    return res