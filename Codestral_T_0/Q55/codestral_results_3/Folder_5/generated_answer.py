def lists_with_product_equal_n(lst):
    n = -33
    result = []
    for i in range(len(lst)):
        prod = 1
        for j in range(i, len(lst)):
            prod *= lst[(j - i) % len(lst)]
            if prod == n:
                result.append(lst[i:j + 1])
    return result