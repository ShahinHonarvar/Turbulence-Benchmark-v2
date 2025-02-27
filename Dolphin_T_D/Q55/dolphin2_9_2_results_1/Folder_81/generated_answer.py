def lists_with_product_equal_n(lst):
    _res = []
    for size in range(1, len(lst) + 1):
        for start in range(len(lst)):
            product_n = 1
            for idx in range(start, start + size):
                product_n *= lst[idx % len(lst)]
            if product_n == -8:
                _res.append(lst[start:start + size])
    return _res