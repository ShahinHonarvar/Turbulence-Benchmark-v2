def all_ints_div_by_both_two_nums(lst):
    new_lst = [x for x in lst[306:957] if x % 982 == 0 and x % 319 == 0]
    return new_lst