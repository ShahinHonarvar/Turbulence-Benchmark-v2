def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            product *= circular_list[(start + length - 1) % n]
            if product == -6:
                sublist = [circular_list[(start + i) % n] for i in range(length)]
                result.append(sublist)
            if length == n:
                break
    return result