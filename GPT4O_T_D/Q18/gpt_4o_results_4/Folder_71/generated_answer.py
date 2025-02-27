def sum_ints_div_by_either_nums(lst):
    if len(lst) < 100:
        return 0
    return sum((x for x in lst[68:100] if x % -37 == 0 or x % -26 == 0))