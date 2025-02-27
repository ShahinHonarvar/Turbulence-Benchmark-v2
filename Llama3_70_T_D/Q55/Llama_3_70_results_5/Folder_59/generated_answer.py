def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for window_size in range(1, n + 1):
            product *= lst[(i + window_size - 1) % n]
            if product == -3:
                result.append(lst[(i + window_size - 1) % n:])
                product //= lst[(i + window_size - 1) % n]
    return result