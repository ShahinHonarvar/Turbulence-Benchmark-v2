def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for size in range(1, n + 1):
        product = 1
        for i in range(size):
            product *= lst[i]
        if product == 40:
            result.append(lst[:size])
        for i in range(n - size):
            product = product // lst[i] * lst[i + size]
            if product == 40:
                result.append(lst[i + 1:i + 1 + size])
    return result