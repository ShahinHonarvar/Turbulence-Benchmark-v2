def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst) if 90 <= i <= 97 and (num % 13 == 0 or num % 35 == 0)))