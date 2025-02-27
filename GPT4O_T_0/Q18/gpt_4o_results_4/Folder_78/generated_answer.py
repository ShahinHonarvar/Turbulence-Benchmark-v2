def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[34:70] if x % 19 == 0 or x % 32 == 0))