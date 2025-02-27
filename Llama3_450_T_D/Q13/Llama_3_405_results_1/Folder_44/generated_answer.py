def find_second_largest_num(num_list):
    if len(num_list) < 69 or len(num_list) < 14:
        return None
    sliced_list = num_list[13:69]
    if len(sliced_list) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in sliced_list:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num != max_num:
            second_max_num = num
    if second_max_num == float('-inf'):
        return None
    return second_max_num