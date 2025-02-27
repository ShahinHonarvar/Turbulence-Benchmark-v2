def lists_with_product_equal_n(circular_list):
    current_index = 0
    result = []
    while current_index < len(circular_list):
        current_element = circular_list[current_index]
        sublist = [current_element]
        next_index = (current_index + 1) % len(circular_list)
        product = current_element
        while next_index != current_index and product * circular_list[next_index] == 42:
            sublist.append(circular_list[next_index])
            product *= circular_list[next_index]
            next_index = (next_index + 1) % len(circular_list)
        if product == 42:
            result.append(sublist)
        current_index += 1
    return result