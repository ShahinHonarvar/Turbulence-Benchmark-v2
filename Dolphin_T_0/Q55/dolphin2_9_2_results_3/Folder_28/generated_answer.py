def lists_with_product_equal_n(lst):
    product_n = 85
    n = len(lst)
    lst_circular = lst + lst[:2]
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i + n):
            product *= lst_circular[j]
            sublist.append(lst_circular[j])
            if product == product_n:
                result.append(sublist)
            elif product > product_n:
                break
    return result