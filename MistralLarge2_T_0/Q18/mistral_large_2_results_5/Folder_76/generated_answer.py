def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[250:630] if x % 850 == 0 or x % 587 == 0))