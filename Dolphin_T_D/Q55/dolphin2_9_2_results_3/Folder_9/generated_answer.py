def lists_with_product_equal_n(lst, n=-36):
    if not lst:
        return []
    result = []
    product = 1
    for i in range(len(lst)):
        product *= lst[i]
        if product == n:
            result.append(lst[:i + 1])
        for j in range(i + 1, len(lst)):
            product = 1
            for k in range(i, j + 1):
                product *= lst[k]
                if product == n:
                    result.append(lst[i:j + 2])
    return result