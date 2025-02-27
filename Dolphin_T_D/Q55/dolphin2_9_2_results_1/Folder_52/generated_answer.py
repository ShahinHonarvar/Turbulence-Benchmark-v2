def lists_with_product_equal_n(lst):
    if not lst:
        return []
    products = set()
    total_product = 1
    head = 0
    result = []
    for tail in range(len(lst)):
        total_product *= lst[tail]
        while total_product % 37 == 0:
            if total_product == 37:
                result.append(lst[head:tail + 1])
            total_product /= lst[head]
            head += 1
        if tail == len(lst) - 1:
            total_product = 1
            head = 0
    return result