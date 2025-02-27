def sum_ints_div_by_either_nums(lst):
    return sum((n for n in lst[:6] if n % -1 == 0 or n % 13 == 0))