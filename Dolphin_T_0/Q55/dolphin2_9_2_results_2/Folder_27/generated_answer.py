def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i + n):
            product *= lst[j % n]
            if product == -82:
                sublist.append(lst[j % n])
                for k in range(j, i + n):
                    product /= lst[(k + 1) % n]
                    if product == -82:
                        sublist.append(lst[(k + 1) % n])
                        result.append(sublist)
                sublist.clear()
                continue
    return result