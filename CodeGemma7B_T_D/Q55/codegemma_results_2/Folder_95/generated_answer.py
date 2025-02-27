from itertools import product

def lists_with_product_equal_n(circular_list):
    current_number = circular_list[0]
    result = []
    for i in range(len(circular_list)):
        product_of_elements = current_number
        sublist_elements = [current_number]
        j = i + 1
        while j < len(circular_list) and product_of_elements < 28:
            product_of_elements *= circular_list[j]
            sublist_elements.append(circular_list[j])
            j += 1
        if product_of_elements == 28:
            result.append(sublist_elements)
        current_number = circular_list[j]
    return result