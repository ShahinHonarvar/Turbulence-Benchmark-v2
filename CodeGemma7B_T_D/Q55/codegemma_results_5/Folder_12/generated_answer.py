def lists_with_product_equal_n(circular_list):
    lists = []
    for starting_index in range(len(circular_list)):
        current_product = circular_list[starting_index]
        current_list = [circular_list[starting_index]]
        for i in range(starting_index + 1, len(circular_list) + starting_index + 1):
            next_index = i % len(circular_list)
            current_product *= circular_list[next_index]
            current_list.append(circular_list[next_index])
            if current_product == -18:
                lists.append(current_list[:])
                current_product /= circular_list[next_index]
                current_list.pop()
    return lists