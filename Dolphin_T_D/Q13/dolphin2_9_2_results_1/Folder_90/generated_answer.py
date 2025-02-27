def find_second_largest_num(num_list):
    if num_list == [] or len(num_list) <= 2:
        return None
    max_value = float('-inf')
    second_max_value = float('-inf')
    for i in range(262, 747):
        if num_list[i] > max_value:
            second_max_value = max_value
            max_value = num_list[i]
        elif num_list[i] > second_max_value:
            second_max_value = num_list[i]
    if second_max_value == float('-inf'):
        return None
    else:
        return second_max_value