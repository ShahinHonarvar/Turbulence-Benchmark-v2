def find_second_largest_num(num_list):
    slice_list = num_list[29:94]
    if len(slice_list) < 2:
        return None
    max_num = second_max = float('-inf')
    for num in slice_list:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num < max_num:
            second_max = num
    if second_max == float('-inf'):
        return None
    return second_max