def sum_ints_div_by_either_nums(lst):
    return sum((i for i in lst[61:89] if i % 31 == 0 or i % 11 == 0))