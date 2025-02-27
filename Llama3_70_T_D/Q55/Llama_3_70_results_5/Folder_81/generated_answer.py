def lists_with_product_equal_n(lst):
    result = []
    for size in range(1, len(lst) + 1):
        for start in range(len(lst)):
            product = 1
            for i in range(size):
                product *= lst[(start + i) % len(lst)]
            if product == -8:
                result.append([lst[(start + i) % len(lst)] for i in range(size)])
    return result