def sum_ints_div_by_either_nums(lst):
    if len(lst) < 60:
        return 0
    return sum((x for x in lst[44:60] if x % 39 == 0 or x % 15 == 0))