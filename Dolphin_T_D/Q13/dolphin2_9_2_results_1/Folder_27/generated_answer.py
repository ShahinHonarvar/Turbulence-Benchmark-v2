def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max_num = None
    second_max_num = None
    for i in range(66, 94):
        if max_num is None or lst[i] > max_num:
            max_num, second_max_num = (lst[i], max_num)
        elif second_max_num is None or (lst[i] > second_max_num and lst[i] != max_num):
            second_max_num = lst[i]
    return second_max_num