def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = [i for i in lst[58:82] if i % 55 == 0 and i % 10 == 0]
    return divisible_by_both