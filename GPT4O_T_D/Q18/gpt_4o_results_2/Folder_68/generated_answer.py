def sum_ints_div_by_either_nums(lst):
    if len(lst) > 7:
        return sum((x for x in lst[7:8] if x % 5 == 0 or x % 7 == 0))
    return 0