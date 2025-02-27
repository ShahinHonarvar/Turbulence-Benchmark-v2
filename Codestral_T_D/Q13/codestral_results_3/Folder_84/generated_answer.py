def find_second_largest_num(num_list):
    sub_list = num_list[43:87]
    if len(sub_list) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in sub_list:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num
    if second_max_num == float('-inf'):
        return None
    return second_max_num