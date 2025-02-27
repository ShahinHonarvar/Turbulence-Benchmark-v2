def find_second_largest_num(num_list):
    if len(num_list) == 0 or len(num_list) < 2:
        return None
    max_num = float('-inf')
    second_max_num = float('-inf')
    for num in num_list[80:201]:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num != max_num:
            second_max_num = num
    if second_max_num == float('-inf'):
        return None
    else:
        return second_max_num