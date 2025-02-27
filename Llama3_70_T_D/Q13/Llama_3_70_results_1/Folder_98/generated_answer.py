def find_second_largest_num(num_list):
    if len(num_list) <= 1:
        return None
    max_num = second_max = float('-inf')
    for i in range(7):
        if num_list[i] > max_num:
            second_max = max_num
            max_num = num_list[i]
        elif num_list[i] > second_max and num_list[i] != max_num:
            second_max = num_list[i]
    if second_max == float('-inf'):
        return None
    return second_max