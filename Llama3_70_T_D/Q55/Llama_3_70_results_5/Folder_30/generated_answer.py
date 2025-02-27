def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(1, n + 1):
            product *= lst[(i + j - 1) % n]
            if product > 99:
                break
            if product == 99:
                result.append((lst[(i + j - 1) % n] for _ in range(j)))
    return result