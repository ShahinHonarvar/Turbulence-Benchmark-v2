def all_ints_div_by_num(lst):
    divisible_nums = [num for num in lst[12:93] if num % -14 == 0]
    return divisible_nums if divisible_nums else []