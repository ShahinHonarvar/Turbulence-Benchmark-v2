def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[306:958] if x % 982 == 0 or x % 319 == 0))