def sum_ints_div_by_either_nums(lst):
    return sum((num for num in lst[35:65] if num % -30 == 0 or num % -95 == 0))