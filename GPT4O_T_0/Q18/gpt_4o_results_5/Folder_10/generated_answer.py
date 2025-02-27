def sum_ints_div_by_either_nums(lst):
    if len(lst) < 100:
        return 0
    return sum((x for x in lst[32:100] if x % -11 == 0 or x % -15 == 0))