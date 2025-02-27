def sum_ints_div_by_either_nums(lst):
    if len(lst) < 799:
        return 0
    return sum((x for x in lst[154:799] if x % 275 == 0 or x % 580 == 0))