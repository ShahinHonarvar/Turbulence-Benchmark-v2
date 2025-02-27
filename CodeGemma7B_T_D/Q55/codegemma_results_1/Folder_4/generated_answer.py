def lists_with_product_equal_n(circular_list):
    product = 91
    product_list = []
    current_list = []
    for element in circular_list:
        current_list.append(element)
        current_product = 1
        for num in current_list:
            current_product *= num
        if current_product == product:
            product_list.append(current_list.copy())
        if current_product > product:
            current_list.pop(0)
    return product_list