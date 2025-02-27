def lists_with_product_equal_n(circular_list):
    multiple_products_of_2 = []
    current_product = 1
    left_pointer = 0
    right_pointer = 0
    while right_pointer < len(circular_list):
        current_product *= circular_list[right_pointer]
        while current_product > 2 and left_pointer <= right_pointer:
            current_product /= circular_list[left_pointer]
            left_pointer += 1
        if current_product == 2:
            current_sublist = circular_list[left_pointer:right_pointer + 1]
            multiple_products_of_2.append(current_sublist)
        right_pointer += 1
    return multiple_products_of_2