def lists_with_product_equal_n(lst):
    n = -89
    result = []
    for i in range(len(lst)):
        prod = 1
        sublist = []
        for j in range(i, len(lst) + i):
            prod *= lst[j % len(lst)]
            sublist.append(lst[j % len(lst)])
            if prod == n:
                result.append(sublist)
            if prod > n:
                break
    return result