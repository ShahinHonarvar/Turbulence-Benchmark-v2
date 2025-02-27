def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            end = (start + length - 1) % n
            product *= lst[end]
            if product == -10:
                result.append(lst[start:end] if end > start else lst[start:] + lst[:end])
    return result