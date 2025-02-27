def sum_ints_div_by_either_nums(lst):
    if len(lst) == 0:
        return 0
    if lst[0] % 1 == 0 or lst[0] % -1 == 0:
        return lst[0]
    return 0