def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    if n == 0:
        return result
    product = 1
    for i in range(n):
        product *= lst[i]
    if product != -968:
        return result
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= lst[j % n]
            if product == -968:
                result.append(lst[i:j + 1])
    return result