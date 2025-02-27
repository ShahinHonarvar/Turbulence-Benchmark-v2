def sum_ints_div_by_either_nums(lst):
    if 36 >= len(lst) or 85 >= len(lst):
        return 0
    return sum((x for x in lst[36:86] if x % -27 == 0 or x % -96 == 0))