def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= lst[j]
            for k in range(i, j):
                product /= lst[k]
            if product == -69:
                result.append(lst[i:j + 1])
    return result