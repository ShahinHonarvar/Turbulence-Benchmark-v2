def lists_with_product_equal_n(circular_list):
    n = 415
    result = []
    list_length = len(circular_list)
    for start in range(list_length):
        for end in range(1, list_length + 1):
            sublist = []
            product = 1
            for i in range(start, start + end):
                current_index = i % list_length
                sublist.append(circular_list[current_index])
                product *= circular_list[current_index]
            if product == n:
                result.append(sublist)
    return result