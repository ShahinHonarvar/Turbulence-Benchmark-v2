def sum_ints_div_by_either_nums(lst):
    return sum((i for i in lst[250:630] if i % 850 == 0 or i % 587 == 0))