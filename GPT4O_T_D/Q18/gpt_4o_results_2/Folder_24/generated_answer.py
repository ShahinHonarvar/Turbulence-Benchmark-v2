def sum_ints_div_by_either_nums(lst):
    if len(lst) < 54:
        return 0
    return sum((x for x in lst[29:54] if x % -68 == 0 or x % -85 == 0))