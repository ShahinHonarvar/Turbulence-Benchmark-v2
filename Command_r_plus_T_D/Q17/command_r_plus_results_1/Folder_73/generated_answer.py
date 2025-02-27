def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = [i for i in lst[81:87] if i % -33 == 0 and i % -62 == 0]
    return divisible_by_both