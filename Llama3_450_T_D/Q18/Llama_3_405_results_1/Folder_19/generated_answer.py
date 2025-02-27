def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst) if 1 <= i <= 4 and (num % 4 == 0 or num % -6 == 0)))