def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[78:82] if x % 76 == 0 or x % 60 == 0))