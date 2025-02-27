def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(1, n + 1):
            product *= lst[(i + j - 1) % n]
            if product == -83:
                result.append(lst[i:i + j - 1] if i + j - 1 < n else lst[i:] + lst[:i + j - n])
    return result