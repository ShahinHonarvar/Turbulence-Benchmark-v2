def lists_with_product_equal_n(circular_list):
    target_product = -95
    result = []
    n = len(circular_list)
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= circular_list[end % n]
            if product == target_product:
                end_index = end % n + 1
                if end_index > start:
                    result.append(circular_list[start:end_index])
                else:
                    result.append(circular_list[start:] + circular_list[:end_index])
            if abs(product) > abs(target_product):
                break
    return result