def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for window_size in range(1, n + 1):
        for i in range(n):
            product = 1
            for j in range(window_size):
                product *= lst[(i + j) % n]
            if product == -23:
                result.append(lst[i:i + window_size])
    return result