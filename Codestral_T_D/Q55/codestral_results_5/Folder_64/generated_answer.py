def lists_with_product_equal_n(lst):
    n = 3
    result = []
    lst += lst
    for i in range(len(lst)):
        product = 1
        sublist = []
        for j in range(i, len(lst)):
            product *= lst[j]
            sublist.append(lst[j])
            if product == n:
                result.append(sublist)
            if product > n:
                break
    return result