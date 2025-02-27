def lists_with_product_equal_n(circular_list):
    if not circular_list:
        return []
    result = []
    n = len(circular_list)
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            product *= circular_list[(start + length - 1) % n]
            if product == -16:
                result.append([circular_list[(start + i) % n] for i in range(length)])
            if length == n:
                break
    return result