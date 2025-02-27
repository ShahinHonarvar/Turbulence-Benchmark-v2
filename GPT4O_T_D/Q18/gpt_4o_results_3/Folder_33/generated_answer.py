def sum_ints_div_by_either_nums(lst):
    return sum((n for n in lst[281:695] if n % -722 == 0 or n % -731 == 0))