def sum_ints_div_by_either_nums(lst):
    if len(lst) < 9:
        return 0
    return sum((x for x in lst[1:9] if x % 9 == 0 or x % 3 == 0))