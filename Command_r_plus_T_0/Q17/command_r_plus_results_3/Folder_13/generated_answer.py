def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = [i for i in lst[13:19] if i % 45 == 0 and i % 20 == 0]
    return divisible_by_both