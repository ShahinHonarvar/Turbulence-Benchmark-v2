def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for size in range(1, n + 1):
        product = 1
        for i in range(size):
            product *= lst[i]
        if product == -51:
            result.append(lst[:size])
        for i in range(n):
            product = product / lst[i] * lst[(i + size) % n]
            if product == -51:
                result.append([lst[(i + j) % n] for j in range(size)])
    return result