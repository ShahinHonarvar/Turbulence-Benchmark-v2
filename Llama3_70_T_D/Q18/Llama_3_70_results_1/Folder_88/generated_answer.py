def sum_ints_div_by_either_nums(lst):
    return sum((num for num in lst[3:10] if num % 6 == 0 or num % 1 == 0))