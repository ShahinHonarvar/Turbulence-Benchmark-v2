def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    product = 1
    for i in range(1, n + 1):
        product *= lst[i % n]
    if product != 13:
        return []
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= lst[j % n]
            if product == 13:
                result.append(list(lst[i % n:j % n + 1]))
    return result