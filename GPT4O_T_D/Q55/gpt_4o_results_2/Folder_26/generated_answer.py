def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            idx = (start + size - 1) % n
            product *= circular_list[idx]
            if product == 93:
                end_idx = (start + size) % n
                if end_idx > start:
                    sublist = circular_list[start:end_idx]
                else:
                    sublist = circular_list[start:] + circular_list[:end_idx]
                result.append(sublist)
    return result