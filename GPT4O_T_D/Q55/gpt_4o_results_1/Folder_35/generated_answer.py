def lists_with_product_equal_n(circular_list):
    target_product = 83
    n = len(circular_list)
    results = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            product *= circular_list[(start + length - 1) % n]
            if product == target_product:
                end_index = (start + length) % n
                if start < end_index:
                    sublist = circular_list[start:end_index]
                else:
                    sublist = circular_list[start:] + circular_list[:end_index]
                results.append(sublist)
            if length == n:
                break
    return results