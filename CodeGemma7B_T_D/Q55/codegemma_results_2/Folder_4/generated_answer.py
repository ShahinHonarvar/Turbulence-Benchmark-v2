def lists_with_product_equal_n(circular_list):
    current_index = 0
    result = []
    current = circular_list[current_index]
    while True:
        product = current
        current_length = 1
        next_index = current_index + 1
        while next_index != current_index:
            next_value = circular_list[next_index]
            product *= next_value
            current_length += 1
            if product == 91 and current_length <= len(circular_list):
                if current_length == len(circular_list):
                    result.append(circular_list[:])
                else:
                    result.append(circular_list[current_index:next_index + 1])
            current_index = next_index
            current = next_value
            next_index = (next_index + 1) % len(circular_list)
        current_index += 1
        if current_index == len(circular_list):
            break
    return result