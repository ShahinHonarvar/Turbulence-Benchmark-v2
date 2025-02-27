def sum_ints_div_by_either_nums(lst):
    if len(lst) < 93:
        return 0
    return sum((x for x in lst[50:93] if x % -94 == 0 or x % -95 == 0))