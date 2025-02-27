def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = [i for i in lst[:2] if i % -6 == 0 and i % 4 == 0]
    return divisible_by_both