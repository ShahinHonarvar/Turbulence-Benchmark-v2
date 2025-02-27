def find_second_largest_num(num_list):
    if len(num_list) < 60:
        return None
    second_max = float('-inf')
    max_num = num_list[25:60][0]
    for i in range(25, 60):
        if num_list[i] > max_num:
            second_max = max_num
            max_num = num_list[i]
        elif num_list[i] < max_num and num_list[i] > second_max:
            second_max = num_list[i]
    if second_max == float('-inf'):
        return None
    return second_max