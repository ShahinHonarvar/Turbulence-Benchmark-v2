def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target_product = -91
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            idx = (start + length - 1) % n
            product *= circular_list[idx]
            if product == target_product:
                sublist = [circular_list[(start + i) % n] for i in range(length)]
                result.append(sublist)
            if product == 0:
                break
    return result