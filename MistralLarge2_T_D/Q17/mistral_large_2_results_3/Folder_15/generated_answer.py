def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if i <= 2 and x % -2 == 0 and (x % 3 == 0)]