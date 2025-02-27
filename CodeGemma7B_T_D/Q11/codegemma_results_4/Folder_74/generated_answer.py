def find_largest_num(num_list):
    max_num = num_list[17]
    for i in range(18, 79):
        if num_list[i] > max_num:
            max_num = num_list[i]
    return max_num