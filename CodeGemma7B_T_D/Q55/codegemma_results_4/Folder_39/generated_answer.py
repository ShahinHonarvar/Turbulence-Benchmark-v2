def lists_with_product_equal_n(circular_list):
    circular_list += circular_list[:4]
    product = 1
    current_list = []
    result_list = []
    for i in range(len(circular_list)):
        if product * circular_list[i] == -46:
            current_list.append(circular_list[i])
            result_list.append(current_list[:])
            product = 1
            current_list = []
        elif product * circular_list[i] != -46 and product != 1:
            current_list.append(circular_list[i])
            product *= circular_list[i]
        elif product == 1:
            current_list = [circular_list[i]]
            product *= circular_list[i]