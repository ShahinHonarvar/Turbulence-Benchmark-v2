def lists_with_product_equal_n(lst):
    n = -10
    results = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[(j - i) % len(lst)]
            if product == n:
                results.append(lst[i:j + 1])
    return results