def lists_with_product_equal_n(circular_list):
    s = 1
    current_list = [circular_list[0]]
    result_list = []
    for i in range(2, len(circular_list) + 1):
        if s == 48:
            while s == 48:
                current_list.pop(0)
                s = 1
                for g in current_list:
                    s *= g
        elif i < len(circular_list):
            new_element = circular_list[i]
            s *= new_element
            current_list.append(new_element)
            result_list.append(current_list[:])
        elif i == len(circular_list) and s != 48:
            current_list.append(circular_list[0])
            s *= circular_list[0]
            current_list.pop(0)
    return result_list