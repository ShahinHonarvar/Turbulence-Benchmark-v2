def find_second_largest_num(num_list):
    if len(num_list) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for i in range(min(8, len(num_list))):
        if num_list[i] > max_num:
            second_max_num = max_num
            max_num = num_list[i]
        elif num_list[i] > second_max_num and num_list[i] != max_num:
            second_max_num = num_list[i]
    if second_max_num == float('-inf'):
        return None
    return second_max_num