def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 2 or max(num_list) == num_list[-1]:
        return None
    max_num = num_list[0]
    second_max_num = None
    for num in num_list[1:]:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num != max_num:
            second_max_num = num
    return second_max_num