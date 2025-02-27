def sum_ints_div_by_either_nums(lst):
    if 86 <= len(lst) - 1 < 89:
        return sum((x for x in lst[86:90] if x % -61 == 0 or x % -79 == 0))
    return 0