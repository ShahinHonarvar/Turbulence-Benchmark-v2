def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            prod = 1
            for k in range(i, j):
                prod *= lst[k % len(lst)]
            if prod == -95:
                result.append(lst[i:j])
    return result