def sum_ints_div_by_either_nums(lst):
    if len(lst) < 36:
        return 0
    return sum((x for x in lst[36:86] if x % -27 == 0 or x % -96 == 0))