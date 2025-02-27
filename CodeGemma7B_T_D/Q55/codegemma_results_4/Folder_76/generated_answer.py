def lists_with_product_equal_n(circular_list):
    circular_list.append(circular_list[0])
    if len(circular_list) < 6:
        return []
    for i in range(1, len(circular_list) - 5):
        if circular_list[i] * circular_list[i + 1] * circular_list[i + 2] * circular_list[i + 3] * circular_list[i + 4] == 247:
            return [circular_list[i:i + 5]]
        if circular_list[i] * circular_list[i + 1] * circular_list[i + 2] * circular_list[i + 3] * circular_list[i + 4] * circular_list[i + 5] == 247:
            return [circular_list[i:i + 6]]
    return []