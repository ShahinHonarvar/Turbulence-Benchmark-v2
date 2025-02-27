def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    lst_extended = lst + lst
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i + n):
            product *= lst_extended[j]
            sublist.append(lst_extended[j])
            if product == 632:
                result.append(sublist)
            if product >= 632:
                break
    return result