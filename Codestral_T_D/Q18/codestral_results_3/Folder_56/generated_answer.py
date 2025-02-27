def sum_ints_div_by_either_nums(lst):
    return sum((num for num in lst[7:10] if num % -9 == 0 or num % -7 == 0))