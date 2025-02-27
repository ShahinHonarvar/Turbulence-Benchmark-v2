def sum_ints_div_by_either_nums(lst):
    if len(lst) < 85:
        return 0
    return sum((x for x in lst[55:85] if x % -24 == 0 or x % -11 == 0))