def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst) if 81 <= i <= 89 and (num % 56 == 0 or num % 68 == 0)))