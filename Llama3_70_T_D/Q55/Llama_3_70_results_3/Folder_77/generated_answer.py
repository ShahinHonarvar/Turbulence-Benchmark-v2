def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(1, n + 1):
            product *= lst[(i + j - 1) % n]
            if product == 632:
                result.append(lst[(i + j - 1) % n:(i + j) % n] if i + j <= n else lst[(i + j - 1) % n:] + lst[:(i + j) % n])
            if product > 632:
                break
    return result