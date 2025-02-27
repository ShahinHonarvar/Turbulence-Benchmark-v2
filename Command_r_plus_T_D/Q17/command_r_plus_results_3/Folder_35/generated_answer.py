def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = [i for i in lst[77:88] if i % 23 == 0 and i % 57 == 0]
    return divisible_by_both