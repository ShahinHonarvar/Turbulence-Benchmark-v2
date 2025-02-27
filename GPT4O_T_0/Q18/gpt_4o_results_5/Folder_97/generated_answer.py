def sum_ints_div_by_either_nums(lst):
    if len(lst) < 76:
        return 0
    return sum((x for x in lst[58:76] if x % 72 == 0 or x % 62 == 0))