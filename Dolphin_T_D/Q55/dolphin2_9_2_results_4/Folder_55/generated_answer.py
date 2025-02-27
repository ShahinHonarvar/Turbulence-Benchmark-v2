def lists_with_product_equal_n(lst, n=-6):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j + 1])
    for i in range(len(lst)):
        product = 1
        for j in range(i, -1, -1):
            product *= lst[j]
            if product == n:
                result.append(lst[j:i + 1])
    return list(set([tuple(lst) for lst in result]))