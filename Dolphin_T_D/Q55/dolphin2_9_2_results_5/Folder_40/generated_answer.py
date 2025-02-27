def lists_with_product_equal_n(lst):
    if not lst or len(lst) == 1:
        return []
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, n + i):
            product *= lst[j % n]
            sublist.append(lst[j % n])
            if product == -9:
                result.append(sublist)
    return result