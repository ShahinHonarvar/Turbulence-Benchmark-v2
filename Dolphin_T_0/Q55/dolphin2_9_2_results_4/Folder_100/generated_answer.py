def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    result = []
    for i in range(n):
        product = lst[i]
        for j in range(i + 1, n + 1):
            product *= lst[j % n]
            if product > 48:
                break
            if product == 48:
                result.append(lst[i:j])
    return result