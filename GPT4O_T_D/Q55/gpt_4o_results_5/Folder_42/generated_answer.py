def lists_with_product_equal_n(circular_list):
    n = 25
    size = len(circular_list)
    result = []
    for start in range(size):
        product = 1
        for length in range(size):
            idx = (start + length) % size
            product *= circular_list[idx]
            if product == n:
                result.append([circular_list[(start + i) % size] for i in range(length + 1)])
    return result