def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst) if 7 <= i <= 9 and (num % 2 == 0 or num % 3 == 0)))