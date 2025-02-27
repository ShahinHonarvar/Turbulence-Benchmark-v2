def find_second_largest_num(num_list):
    sub_list = num_list[56:99]
    if len(sub_list) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in sub_list:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif max_num > num > second_max_num:
            second_max_num = num
    return second_max_num if second_max_num != float('-inf') else None