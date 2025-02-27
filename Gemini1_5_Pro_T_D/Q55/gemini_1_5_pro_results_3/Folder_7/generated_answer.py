def lists_with_product_equal_n(circular_list):
    n = 537
    result = []
    for start_index in range(len(circular_list)):
        for end_index in range(start_index, start_index + len(circular_list)):
            sublist = circular_list[start_index:end_index % len(circular_list) + 1]
            if start_index > end_index % len(circular_list):
                sublist += circular_list[:end_index % len(circular_list) + 1]
            product = 1
            for x in sublist:
                product *= x
            if product == n:
                result.append(sublist)
    return result