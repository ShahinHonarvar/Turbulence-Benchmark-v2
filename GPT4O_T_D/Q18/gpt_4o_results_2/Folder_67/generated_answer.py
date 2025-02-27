def sum_ints_div_by_either_nums(lst):
    if len(lst) <= 24:
        return 0
    return sum((x for x in lst[24:33] if x % 35 == 0 or x % 87 == 0))