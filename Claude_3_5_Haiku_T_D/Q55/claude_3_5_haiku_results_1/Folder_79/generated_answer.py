def lists_with_product_equal_n(circular_list):
    n = -83
    result = []
    list_length = len(circular_list)
    for start in range(list_length):
        for end in range(start, start + list_length):
            current_sublist = []
            current_product = 1
            for i in range(start, end + 1):
                index = i % list_length
                current_sublist.append(circular_list[index])
                current_product *= circular_list[index]
            if current_product == n and len(current_sublist) > 0:
                result.append(current_sublist)
    return result