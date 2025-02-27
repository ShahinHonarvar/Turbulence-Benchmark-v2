def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for length in range(n):
            product *= circular_list[(start + length) % n]
            if product == 4:
                result.append([circular_list[(start + i) % n] for i in range(length + 1)])
            if product == 0:
                break
    return result