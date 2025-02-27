def sum_ints_div_by_either_nums(lst):
    if len(lst) < 85:
        return 0
    return sum((i for i in lst[57:85] if i % -30 == 0 or i % -88 == 0))