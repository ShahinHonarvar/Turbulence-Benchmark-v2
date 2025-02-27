def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for window_size in range(1, n + 1):
            product *= lst[(i + window_size - 1) % n]
            if product == -57:
                result.append(lst[(i + window_size - window_size) % n:(i + window_size) % n])
    return result