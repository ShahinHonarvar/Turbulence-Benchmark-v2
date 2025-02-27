def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            idx = (start + size - 1) % n
            product *= circular_list[idx]
            if product == 2:
                sublist = [circular_list[(start + i) % n] for i in range(size)]
                result.append(sublist)
    return result