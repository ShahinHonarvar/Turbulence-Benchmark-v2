def sum_ints_div_by_either_nums(lst):
    if len(lst) < 70:
        return 0
    return sum((x for x in lst[69:71] if x % 72 == 0 or x % 70 == 0))