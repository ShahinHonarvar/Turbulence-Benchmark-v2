def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for size in range(1, n + 1):
        for i in range(n):
            product = 1
            for j in range(size):
                product *= lst[(i + j) % n]
            if product == 632:
                result.append(lst[i:i + size] if i + size <= n else lst[i:] + lst[:i + size - n])
    return result