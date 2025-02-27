def lists_with_product_equal_n(lst, n=-6):
    if len(lst) == 0:
        return []
    result = []
    lst_circular = lst + [lst[0]]
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst_circular)):
            product *= lst_circular[j]
            if product == n:
                sublist = lst_circular[i:j + 1]
                result.append(sublist)
    return result