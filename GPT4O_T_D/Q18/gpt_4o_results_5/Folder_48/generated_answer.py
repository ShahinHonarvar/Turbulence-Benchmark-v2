def sum_ints_div_by_either_nums(lst):
    if not lst or len(lst) < 958:
        return 0
    return sum((x for x in lst[306:958] if x % 982 == 0 or x % 319 == 0))