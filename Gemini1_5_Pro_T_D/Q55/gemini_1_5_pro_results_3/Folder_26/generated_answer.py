def lists_with_product_equal_n(circular_list):
    n = 93
    result = []
    list_length = len(circular_list)
    for start_index in range(list_length):
        for end_index in range(start_index, start_index + list_length):
            sublist = circular_list[start_index:end_index + 1]
            if len(sublist) > list_length:
                break
            product = 1
            for x in sublist:
                product *= x
            if product == n:
                result.append(sublist)
    return result