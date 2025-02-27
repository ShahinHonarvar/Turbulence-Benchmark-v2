def lists_with_product_equal_n(lst):
    results = []
    for i in range(len(lst) - 1):
        for j in range(i + 2, len(lst) + 1):
            product = 1
            for k in range(i, j):
                product *= lst[k]
            if product == -82:
                results.append(lst[i:j])
    return results