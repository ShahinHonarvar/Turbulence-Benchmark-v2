def all_ints_div_by_both_two_nums(lst):
    divisible_by_15_and_57 = [i for i in lst[18:53] if i % 15 == 0 and i % 57 == 0]
    return divisible_by_15_and_57