def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = [i for i in lst[306:958] if i % 982 == 0 and i % 319 == 0]
    return divisible_by_both