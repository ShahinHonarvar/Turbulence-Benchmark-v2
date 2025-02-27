def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target_product = -57
    results = []
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            index = end % n
            product *= circular_list[index]
            if product == target_product:
                end_index = index + 1 if index >= start else n + index + 1
                results.append(circular_list[start:end_index] if end_index <= n else circular_list[start:] + circular_list[:end_index % n])
            if product == 0:
                break
    return results