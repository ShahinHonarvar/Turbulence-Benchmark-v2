def find_second_largest_num(lst):
    if len(lst) == 0:
        return None
    max_num = None
    second_max = None
    for i in range(4, 9):
        if lst[i] > max_num or max_num is None:
            second_max = max_num
            max_num = lst[i]
        elif lst[i] > second_max or second_max is None:
            second_max = lst[i]
    return second_max