def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for size in range(1, n + 1):
        for i in range(n):
            product = 1
            for j in range(size):
                product *= lst[(i + j) % n]
            if product == -36:
                result.append(lst[i:i + size])
    return result