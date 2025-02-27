def find_second_largest_num(num_list):
    if len(num_list) < 2:
        return None
    sliced_list = num_list[59:98]
    if len(sliced_list) < 2:
        return None
    max_num = second_max = float('-inf')
    for num in sliced_list:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num < max_num:
            second_max = num
    if second_max == float('-inf'):
        return None
    return second_max