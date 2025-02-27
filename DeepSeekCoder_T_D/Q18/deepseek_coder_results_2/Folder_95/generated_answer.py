def sum_ints_div_by_either_nums(lst):
    if len(lst) < 85:
        return 0
    return sum((x for x in lst[57:85] if x % -30 == 0 or x % -88 == 0))