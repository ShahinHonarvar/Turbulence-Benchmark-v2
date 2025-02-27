def sum_ints_div_by_either_nums(lst):
    if len(lst) == 0:
        return 0
    elif lst[0] == 1 or lst[0] == -1:
        return lst[0]
    else:
        return 0