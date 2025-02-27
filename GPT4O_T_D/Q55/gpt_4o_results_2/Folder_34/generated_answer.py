def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            idx = (start + length - 1) % n
            product *= circular_list[idx]
            if product == -81:
                end_idx = (start + length) % n
                if end_idx > start:
                    result.append(circular_list[start:end_idx])
                else:
                    result.append(circular_list[start:] + circular_list[:end_idx])
    return result