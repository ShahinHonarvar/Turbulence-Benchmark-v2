def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[50:201] if x % -34 == 0 or x % 64 == 0))