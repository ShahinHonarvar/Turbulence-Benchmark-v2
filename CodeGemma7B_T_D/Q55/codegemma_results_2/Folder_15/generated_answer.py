def lists_with_product_equal_n(circular_list, target_product):
    current_product = 1
    current_list = []
    result = []
    for element in circular_list + circular_list:
        current_product *= element
        current_list.append(element)
        while current_product > target_product:
            current_product //= current_list.pop(0)
        if current_product == target_product:
            result.append(current_list[:])
    return result