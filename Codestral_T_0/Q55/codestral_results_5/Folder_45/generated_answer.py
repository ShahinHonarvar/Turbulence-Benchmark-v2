def lists_with_product_equal_n(lst):
    n = -5
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[(j - i) % len(lst)]
            if product == n:
                result.append(lst[i:j + 1])
    return result