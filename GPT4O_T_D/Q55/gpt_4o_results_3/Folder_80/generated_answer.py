def lists_with_product_equal_n(circular_list):
    result = []
    n = 43
    list_len = len(circular_list)
    for start in range(list_len):
        product = 1
        sublist = []
        for index in range(list_len):
            current_index = (start + index) % list_len
            product *= circular_list[current_index]
            sublist.append(circular_list[current_index])
            if product == n:
                result.append(sublist.copy())
            if product == 0 or product > n:
                break
    return result