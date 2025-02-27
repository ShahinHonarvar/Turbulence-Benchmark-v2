def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[25:81]) if x % -20 == 0 or x % -26 == 0))