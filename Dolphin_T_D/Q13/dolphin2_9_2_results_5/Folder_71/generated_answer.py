def find_second_largest_num(lst):
    if len(lst) == 0:
        return None
    max_num = None
    second_max_num = None
    for i in range(26, 53):
        if lst[i] > max_num:
            second_max_num = max_num
            max_num = lst[i]
        elif lst[i] > second_max_num and lst[i] != max_num:
            second_max_num = lst[i]
    return second_max_num