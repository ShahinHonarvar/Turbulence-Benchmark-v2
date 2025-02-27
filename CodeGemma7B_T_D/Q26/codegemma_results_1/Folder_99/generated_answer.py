def sum_in_range(num_list):
    element_list = [element for element in num_list if element in range(782, 788)]
    if len(element_list) == 0:
        return 0
    else:
        return sum(element_list)