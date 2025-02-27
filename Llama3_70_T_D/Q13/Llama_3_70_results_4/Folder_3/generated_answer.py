def find_second_largest_num(lst):
    slice_list = lst[62:93]
    if len(slice_list) < 2:
        return None
    max_num = second_max = float('-inf')
    for num in slice_list:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num < max_num:
            second_max = num
    return None if second_max == float('-inf') else second_max