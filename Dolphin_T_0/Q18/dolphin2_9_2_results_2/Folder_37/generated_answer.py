def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[1:2] + lst[5:7] if x % -1 == 0 or x % -7 == 0))