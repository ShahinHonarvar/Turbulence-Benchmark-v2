def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    product = 15
    result = []
    for i in range(n):
        product_current = 1
        for j in range(i, n + i):
            product_current *= lst[j % n]
            if product_current == product:
                result.append(lst[i:j + 1])
    return result