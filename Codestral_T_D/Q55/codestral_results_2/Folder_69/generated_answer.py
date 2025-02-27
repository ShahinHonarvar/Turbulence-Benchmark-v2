def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    lst += lst
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i + n):
            product *= lst[j]
            sublist.append(lst[j])
            if product == 90:
                if len(sublist) < n:
                    result.append(sublist)
                product /= sublist[0]
                sublist.pop(0)
            elif product > 90:
                if sublist:
                    product /= sublist.pop(0)
            else:
                continue
    return result