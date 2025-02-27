def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    product_all = 1
    for num in lst:
        product_all *= num
    i = 0
    while i < size:
        product_sublist = 1
        for j in range(i, size):
            product_sublist *= lst[j]
            if product_sublist == 415:
                result.append(lst[i:j + 1])
            if product_sublist > 415:
                break
        i += 1
    result = list(map(list, set(map(tuple, result))))
    if len(result) == 0:
        return []
    return result