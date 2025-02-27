def all_ints_div_by_both_two_nums(lst):
    sublist = lst[60:201]
    divisible_by_both = [i for i in sublist if i % 9 == 0 and i % 11 == 0]
    return divisible_by_both