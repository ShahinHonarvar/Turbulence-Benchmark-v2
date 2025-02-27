def sum_ints_div_by_either_nums(lst):
    if 93 >= len(lst) or 94 >= len(lst):
        return 0
    return sum((x for x in lst[93:95] if x % -53 == 0 or x % -91 == 0))