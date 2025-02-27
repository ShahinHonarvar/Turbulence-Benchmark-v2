def sum_ints_div_by_either_nums(lst):
    return sum((num for num in lst[:10] if num % 10 == 0 or num % 100 == 0))