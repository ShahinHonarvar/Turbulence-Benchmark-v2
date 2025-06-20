def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == -95:
                result.append((lst[(i + k) % n] for k in range(j + 1)))
    return result