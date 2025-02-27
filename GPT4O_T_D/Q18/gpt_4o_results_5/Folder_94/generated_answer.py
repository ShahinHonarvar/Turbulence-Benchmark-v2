def sum_ints_div_by_either_nums(lst):
    if len(lst) < 95:
        return 0
    sublist = lst[93:95]
    return sum((x for x in sublist if x % -53 == 0 or x % -91 == 0))