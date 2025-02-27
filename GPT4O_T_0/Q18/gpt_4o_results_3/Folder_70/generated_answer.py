def sum_ints_div_by_either_nums(lst):
    if len(lst) < 44:
        return 0
    return sum((x for x in lst[42:44] if x % 15 == 0 or x % 87 == 0))