def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[34:82] if x % 27 == 0 or x % 57 == 0))