def find_second_largest_num(num_list):
    specific_range = num_list[262:747]
    if len(specific_range) < 2:
        return None
    max_num = second_max = float('-inf')
    for num in specific_range:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num
    if second_max == float('-inf'):
        return None
    return second_max