def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = [i for i in lst[11:47] if i % 55 == 0 and i % 36 == 0]
    return divisible_by_both