def find_second_largest_num(num_list):
    if len(num_list) < 2:
        return None
    max_num = max(num_list)
    second_max_num = None
    for num in num_list:
        if num != max_num and (second_max_num is None or num > second_max_num):
            second_max_num = num
    return second_max_num