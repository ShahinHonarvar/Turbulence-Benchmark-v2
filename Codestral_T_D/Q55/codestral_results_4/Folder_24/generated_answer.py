def lists_with_product_equal_n(lst):
    n = -89
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = []
        for j in range(i, len(lst)):
            product *= lst[j]
            sublist.append(lst[j])
            if product == n:
                result.append(sublist)
        product = 1
        sublist = []
        for j in range(i):
            product *= lst[j]
            sublist.append(lst[j])
            if product == n:
                result.append(sublist)
    return result