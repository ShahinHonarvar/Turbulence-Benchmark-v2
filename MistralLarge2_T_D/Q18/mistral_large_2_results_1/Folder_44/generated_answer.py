def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[25:71] if x % 74 == 0 or x % 15 == 0))