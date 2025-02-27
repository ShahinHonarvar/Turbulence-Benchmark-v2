def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == 37:
                result.append(lst[i:j + 1])
    return result