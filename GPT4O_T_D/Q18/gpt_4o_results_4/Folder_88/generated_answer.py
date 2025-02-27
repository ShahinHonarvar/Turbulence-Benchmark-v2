def sum_ints_div_by_either_nums(lst):
    if len(lst) < 10:
        return 0
    return sum((x for x in lst[3:10] if x % 6 == 0 or x % 1 == 0))