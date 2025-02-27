def find_second_largest_num(num_list):
    if len(num_list) <= 40 or len(num_list) - 1 < 80:
        return None
    max_num = num_list[40]
    second_max_num = num_list[41] if num_list[40] > num_list[41] else num_list[40]
    for i in range(42, 81):
        if num_list[i] > max_num:
            second_max_num = max_num
            max_num = num_list[i]
        elif num_list[i] > second_max_num:
            second_max_num = num_list[i]
    return second_max_num