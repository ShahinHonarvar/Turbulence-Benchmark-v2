def lists_with_product_equal_n(circular_list):
    current_product = 1
    current_sublist = []
    results = []
    for element in circular_list + circular_list:
        if current_product == 37:
            results.append(current_sublist[:])
        elif current_product < 37:
            current_product *= element
            current_sublist.append(element)
        else:
            current_product //= current_sublist.pop(0)
    return results