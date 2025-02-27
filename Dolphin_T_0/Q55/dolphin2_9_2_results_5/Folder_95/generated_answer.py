def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    result = []
    for i in range(n):
        product = 1 if lst[i] is None else lst[i]
        for j in range(i + 1, n + i):
            product *= lst[j % n]
            if product > 28:
                break
            if product == 28:
                result.append(lst[i:j + 1])
    return result