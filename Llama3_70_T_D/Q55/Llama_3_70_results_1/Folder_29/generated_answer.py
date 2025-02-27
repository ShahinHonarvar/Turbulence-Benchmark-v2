def lists_with_product_equal_n(lst):
    result = []
    for window_size in range(1, len(lst) + 1):
        for i in range(len(lst)):
            product = 1
            for j in range(window_size):
                product *= lst[(i + j) % len(lst)]
            if product == 15:
                result.append([lst[(i + k) % len(lst)] for k in range(window_size)])
    return result