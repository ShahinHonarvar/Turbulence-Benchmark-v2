def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[61:89] if x % 31 == 0 or x % 11 == 0))