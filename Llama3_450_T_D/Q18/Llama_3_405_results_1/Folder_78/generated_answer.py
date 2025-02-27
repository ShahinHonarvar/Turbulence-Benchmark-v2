def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst) if 34 <= i <= 69 and (num % 19 == 0 or num % 32 == 0)))