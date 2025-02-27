def sum_ints_div_by_either_nums(lst):
    if len(lst) < 29:
        return 0
    return sum((x for x in lst[10:29] if x % -61 == 0 or x % -64 == 0))