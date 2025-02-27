def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            idx = end % n
            product *= circular_list[idx]
            if product == -54:
                result.append(circular_list[start:idx + 1] if start <= idx else circular_list[start:] + circular_list[:idx + 1])
    return result