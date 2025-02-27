def all_ints_div_by_both_two_nums(lst):
    range_lst = lst[306:958]
    divisible_by_both = [i for i in range_lst if i % 982 == 0 and i % 319 == 0]
    return divisible_by_both