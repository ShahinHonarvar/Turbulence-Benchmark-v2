def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    for i in range(length):
        product = circular_list[i]
        current_length = 1
        j = i
        while j + current_length < length and product * circular_list[(j + current_length) % length] == -72:
            current_length += 1
            product *= circular_list[(j + current_length) % length]
        if current_length > 1:
            result.append(circular_list[i:(j + current_length) % length])
    return result