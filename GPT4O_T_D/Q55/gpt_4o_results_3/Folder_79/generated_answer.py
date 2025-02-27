def lists_with_product_equal_n(circular_list):
    n = -83
    results = []
    list_len = len(circular_list)
    for start in range(list_len):
        product = 1
        for length in range(1, list_len + 1):
            end = (start + length) % list_len
            product *= circular_list[(start + length - 1) % list_len]
            if length > list_len:
                break
            if product == n:
                if end > start:
                    results.append(circular_list[start:end])
                else:
                    results.append(circular_list[start:] + circular_list[:end])
    return results