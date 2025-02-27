def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = [i for i in lst[78:82] if i % 76 == 0 and i % 60 == 0]
    return divisible_by_both