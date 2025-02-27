def sum_ints_div_by_either_nums(lst):
    return sum((num for num in lst[50:93] if num % -94 == 0 or num % -95 == 0))