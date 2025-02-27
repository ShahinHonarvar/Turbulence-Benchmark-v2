def lists_with_product_equal_n(circular_list):
    if not circular_list or len(circular_list) == 1:
        return []
    result = []
    for i in range(1, len(circular_list)):
        current_element = circular_list[i]
        previous_element = circular_list[i - 1]
        product = current_element * previous_element
        if product == 42:
            sublist = [current_element, previous_element]
            result.append(sublist)
        elif product < 42:
            sublist = [current_element]
            result.append(sublist)
        else:
            sublist = []
            product = current_element * previous_element * circular_list[0]
            if product == 42:
                sublist = [current_element, previous_element, circular_list[0]]
                result.append(sublist)
            elif product < 42:
                sublist = [current_element]
                result.append(sublist)
    return result