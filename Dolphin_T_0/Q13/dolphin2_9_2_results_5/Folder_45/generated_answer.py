def find_second_largest_num(num_list):
    if len(num_list) < 1:
        return 'None'
    max_num = num_list[30]
    second_max_num = 'None'
    for i in range(31, 201):
        if num_list[i] > max_num:
            second_max_num = max_num
            max_num = num_list[i]
        elif num_list[i] < max_num and num_list[i] > second_max_num or second_max_num == 'None':
            second_max_num = num_list[i]
    if second_max_num == 'None':
        return None
    else:
        return second_max_num