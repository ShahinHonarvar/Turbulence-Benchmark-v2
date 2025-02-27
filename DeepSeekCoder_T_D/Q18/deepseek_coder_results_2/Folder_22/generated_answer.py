def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[40:201] if x % 21 == 0 or x % 71 == 0))