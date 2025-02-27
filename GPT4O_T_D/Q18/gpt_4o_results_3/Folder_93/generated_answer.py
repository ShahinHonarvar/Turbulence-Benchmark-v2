def sum_ints_div_by_either_nums(lst):
    if len(lst) < 90:
        return 0
    return sum((x for x in lst[86:90] if x % -61 == 0 or x % -79 == 0))