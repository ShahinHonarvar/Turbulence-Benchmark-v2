def lists_with_product_equal_n(circular_list):
    target_product = 247
    result = []
    list_size = len(circular_list)
    for start_index in range(list_size):
        product = 1
        for end_index in range(start_index, list_size + start_index):
            product *= circular_list[end_index % list_size]
            if product == target_product:
                result.append(circular_list[start_index:end_index % list_size + 1])
            elif product > target_product:
                break
    return result