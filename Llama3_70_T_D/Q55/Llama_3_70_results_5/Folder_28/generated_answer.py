def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for window_size in range(1, n + 1):
        for i in range(n):
            product = 1
            for j in range(window_size):
                index = (i + j) % n
                product *= lst[index]
            if product == 85:
                result.append([lst[(i + k) % n] for k in range(window_size)])
    return result