def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max_num = lst[0]
    second_max_num = None
    for num in lst:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num != max_num:
            second_max_num = num
    return second_max_num