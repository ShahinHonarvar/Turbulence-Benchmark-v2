def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    lst = lst * 2
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i + n):
            product *= lst[j]
            sublist.append(lst[j])
            if product == -33:
                result.append(sublist)
    return result