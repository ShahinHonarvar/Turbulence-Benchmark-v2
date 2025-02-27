def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = [i for i in lst[:10] if i % 10 == 0 and i % 100 == 0]
    return divisible_by_both