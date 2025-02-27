def sum_ints_div_by_either_nums(lst):
    if not lst or len(lst) < 5:
        return 0
    return sum((x for x in lst[:5] if x % 8 == 0 or x % -3 == 0))