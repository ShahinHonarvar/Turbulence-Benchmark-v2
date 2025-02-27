def lists_with_product_equal_n(circular_list):
    target_product = -20
    result = []
    for start_index in range(len(circular_list)):
        product = 1
        for end_index in range(start_index, len(circular_list) + start_index):
            product *= circular_list[end_index % len(circular_list)]
            if product == target_product:
                sublist = [circular_list[i % len(circular_list)] for i in range(start_index, end_index + 1)]
                result.append(sublist)
            elif product == 0:
                break
    return result