def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst[9:101]) if i in range(81) and x % 10 == 0 and (x % 100 == 0)]