def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    product_n = -16
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, n):
            product *= lst[j]
            sublist.append(lst[j])
            if product == product_n:
                result.append(sublist)
            for k in range(i, n):
                product /= lst[k]
                sublist = sublist[1:]
                if product == product_n:
                    result.append(sublist)
    return result