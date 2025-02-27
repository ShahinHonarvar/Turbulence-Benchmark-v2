def lists_with_product_equal_n(lst):
    if not lst:
        return []
    result = []
    product = 1
    for i in range(len(lst) + 1):
        for j in range(i + 1, len(lst) + 1):
            for k in range(i, j):
                product *= lst[k % len(lst)]
            if product == 33:
                result.append(lst[i:j])
    return result