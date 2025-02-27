def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for window_size in range(1, n + 1):
        for i in range(n):
            product = 1
            window = []
            for j in range(window_size):
                product *= lst[(i + j) % n]
                window.append(lst[(i + j) % n])
            if product == -8:
                result.append(window)
    return result