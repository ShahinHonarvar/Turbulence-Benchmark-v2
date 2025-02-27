def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for size in range(1, n + 1):
        for start in range(n):
            product = 1
            for i in range(size):
                product *= lst[(start + i) % n]
            if product == 40:
                result.append([lst[(start + i) % n] for i in range(size)])
    return result