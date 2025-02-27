def lists_with_product_equal_n(circular_list):
    n = 28
    result = []
    for start_index in range(len(circular_list)):
        for end_index in range(start_index, len(circular_list) + start_index):
            sublist = circular_list[start_index:end_index + 1]
            if end_index >= len(circular_list):
                sublist += circular_list[0:(end_index + 1) % len(circular_list)]
            product = 1
            for x in sublist:
                product *= x
            if product == n:
                result.append(sublist)
    return result