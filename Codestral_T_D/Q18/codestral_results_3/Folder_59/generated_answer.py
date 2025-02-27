def sum_ints_div_by_either_nums(lst):
    return sum((num for num in lst[0:9] if num % -3 == 0 or num % 8 == 0))