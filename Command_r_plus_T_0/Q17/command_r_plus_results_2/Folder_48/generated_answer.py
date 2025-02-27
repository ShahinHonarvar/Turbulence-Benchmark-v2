def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[306:958] if i % 982 == 0 and i % 319 == 0]
    return result