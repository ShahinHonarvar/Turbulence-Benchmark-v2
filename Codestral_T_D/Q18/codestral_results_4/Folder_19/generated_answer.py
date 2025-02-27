def sum_ints_div_by_either_nums(lst):
    return sum((num for num in lst[1:5] if num % 4 == 0 or num % -6 == 0))