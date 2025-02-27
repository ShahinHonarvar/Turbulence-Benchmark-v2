def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for window_size in range(1, n + 1):
        product = 1
        for i in range(window_size):
            product *= lst[i]
        if product == -56:
            result.append(lst[:window_size])
        for i in range(n, n + window_size - 1):
            product = product // lst[i - window_size] * lst[i % n]
            if product == -56:
                result.append(lst[i - window_size + 1:i + 1])
    return result