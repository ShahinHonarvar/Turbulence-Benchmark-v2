def lists_with_product_equal_n(lst):
    n = -41
    result = []
    if len(lst) == 0:
        return result
    lst = lst + lst
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j + 1])
    return [sublist for sublist in result if sublist[:len(sublist) // 2] not in result]