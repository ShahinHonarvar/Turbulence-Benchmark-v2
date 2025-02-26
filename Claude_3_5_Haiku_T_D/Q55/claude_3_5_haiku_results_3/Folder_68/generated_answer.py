def lists_with_product_equal_n(circular_list):
    n = 6
    result = []
    list_length = len(circular_list)
    for start in range(list_length):
        for end in range(start, start + list_length):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                current_index = i % list_length
                sublist.append(circular_list[current_index])
                product *= circular_list[current_index]
            if product == n:
                result.append(sublist)
    return result