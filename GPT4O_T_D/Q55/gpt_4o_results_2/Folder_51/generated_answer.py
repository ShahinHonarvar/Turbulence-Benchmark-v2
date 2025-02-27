def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for start in range(n):
        product = 1
        for length in range(n):
            idx = (start + length) % n
            product *= circular_list[idx]
            if product == -44:
                end = (start + length + 1) % n
                if start < end:
                    results.append(circular_list[start:end])
                else:
                    results.append(circular_list[start:] + circular_list[:end])
    return results