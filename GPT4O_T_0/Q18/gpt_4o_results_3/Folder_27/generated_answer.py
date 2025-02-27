def sum_ints_div_by_either_nums(lst):
    if len(lst) < 36:
        return 0
    return sum((x for x in lst[20:36] if x % -36 == 0 or x % -89 == 0))