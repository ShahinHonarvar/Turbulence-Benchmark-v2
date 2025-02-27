def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    n = -93
    result = []
    for i in range(len(lst)):
        product = lst[i]
        if product == n:
            result.append([lst[i]])
        for j in range(i + 1, len(lst)):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j + 1])
    return result