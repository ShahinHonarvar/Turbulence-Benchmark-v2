def lists_with_product_equal_n(circular_list):
    n = -938
    result = []
    list_length = len(circular_list)
    for start in range(list_length):
        for end in range(start, start + list_length):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                actual_index = current_index % list_length
                sublist.append(circular_list[actual_index])
                product *= circular_list[actual_index]
                if product == n:
                    result.append(sublist.copy())
                    break
                current_index += 1
    return result