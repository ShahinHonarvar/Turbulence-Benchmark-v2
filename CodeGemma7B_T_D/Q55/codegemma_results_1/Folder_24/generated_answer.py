def lists_with_product_equal_n(circular_list):
    product = 1
    current_idx = 0
    result = []
    while current_idx < len(circular_list):
        while product == -89:
            result.append(circular_list[current_idx:current_idx + len(result) + 1])
            product = 1
        if circular_list[current_idx] not in [0, -1]:
            product *= circular_list[current_idx]
            current_idx += 1
        else:
            current_idx += 1
    return result