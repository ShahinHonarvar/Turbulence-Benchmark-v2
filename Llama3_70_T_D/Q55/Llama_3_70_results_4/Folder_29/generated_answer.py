def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for window_size in range(1, n + 1):
        for i in range(n):
            window = lst[i:i + window_size]
            if len(window) < n:
                window += lst[:i]
            product = 1
            for num in window:
                product *= num
            if product == 15:
                result.append(window)
    return result