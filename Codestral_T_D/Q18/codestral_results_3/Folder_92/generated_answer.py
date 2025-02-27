def sum_ints_div_by_either_nums(lst):
    return sum((n for n in lst[0:1] if n % 1 == 0 or n % -1 == 0))