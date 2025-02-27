def sum_ints_div_by_either_nums(lst):
    if len(lst) < 41:
        return 0
    return sum((x for x in lst[40:201] if x % 21 == 0 or x % 71 == 0))