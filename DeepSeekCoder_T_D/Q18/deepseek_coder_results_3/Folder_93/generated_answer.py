def sum_ints_div_by_either_nums(lst):
    if 86 > 89 or 86 >= len(lst) or 89 >= len(lst):
        return 0
    return sum((x for x in lst[86:90] if x % -61 == 0 or x % -79 == 0))