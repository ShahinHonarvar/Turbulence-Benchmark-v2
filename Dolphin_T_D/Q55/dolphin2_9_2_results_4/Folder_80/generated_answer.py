def lists_with_product_equal_n(circular_list):
    if len(circular_list) == 0:
        return []
    if len(circular_list) == 1:
        return [circular_list] if circular_list[0] == 43 else []
    product_equal_n_lists = []
    for i_start in range(len(circular_list)):
        current_value = 1
        for i_end in range(i_start, len(circular_list)):
            current_value *= circular_list[i_end]
            if current_value == 43:
                product_equal_n_lists.append(circular_list[i_start:i_end + 1])
    return list(set(map(tuple, product_equal_n_lists)))