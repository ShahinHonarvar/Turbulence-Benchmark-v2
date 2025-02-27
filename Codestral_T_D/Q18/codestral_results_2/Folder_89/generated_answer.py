def sum_ints_div_by_either_nums(lst):
    return sum((num for num in lst[28:97] if num % 90 == 0 or num % 97 == 0))