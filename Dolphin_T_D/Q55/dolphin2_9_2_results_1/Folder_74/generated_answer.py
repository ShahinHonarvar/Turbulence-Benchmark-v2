def lists_with_product_equal_n(lst):
    if not lst:
        return []
    lst = lst + lst[:2]
    result = []
    for i in range(len(lst) - 2):
        for j in range(i + 2, len(lst)):
            product = 1
            for k in range(i, j + 1):
                product *= lst[k]
            if product == 51:
                result.append(lst[i:j + 1])
    return result