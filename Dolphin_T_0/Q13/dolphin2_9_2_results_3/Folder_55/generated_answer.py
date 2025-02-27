def find_second_largest_num(num_list):
    second_largest = None
    max_value = float('-inf')
    second_max_value = float('-inf')
    for value in num_list[0:11]:
        if value > max_value:
            second_max_value = max_value
            max_value = value
        elif max_value > value > second_max_value:
            second_max_value = value
    if second_max_value != float('-inf'):
        return second_max_value
    else:
        return None