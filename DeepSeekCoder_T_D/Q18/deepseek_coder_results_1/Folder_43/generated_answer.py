def sum_ints_div_by_either_nums(lst):
    if len(lst) < 86:
        return 0
    return sum((x for x in lst[57:86] if x % -77 == 0 or x % -32 == 0))