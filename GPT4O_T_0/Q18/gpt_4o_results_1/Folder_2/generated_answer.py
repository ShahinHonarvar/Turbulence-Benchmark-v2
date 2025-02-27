def sum_ints_div_by_either_nums(lst):
    if len(lst) < 87:
        return 0
    return sum((x for x in lst[73:87] if x % 54 == 0 or x % 82 == 0))