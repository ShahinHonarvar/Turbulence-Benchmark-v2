def find_second_largest_num(lst):
    if len(lst) < 49:
        return None
    slice_of_lst = lst[30:49]
    max_num = second_max_num = float('-inf')
    for num in slice_of_lst:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num
    if second_max_num == float('-inf'):
        return None
    return second_max_num