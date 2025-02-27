def lists_with_product_equal_n(circular_list):
    product = -32
    lists_of_integers = []
    current_list = []
    current_product = 1
    for number in circular_list + circular_list[:len(circular_list) - 1]:
        current_product *= number
        current_list.append(number)
        if current_product == product:
            lists_of_integers.append(current_list[:])
        elif current_product > product:
            current_product = 1
            current_list = []
    return lists_of_integers