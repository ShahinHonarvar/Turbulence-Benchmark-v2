def all_ints_div_by_both_two_nums(lst):
    if len(lst) < 2:
        return []
    return [x for x in lst[0:2] if x % 6 == 0 and x % 4 == 0]