def lists_with_product_equal_n(values):
    return [[i for i, j in enumerate(values) if j == k] for k in [-32]]