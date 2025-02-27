def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst) if 13 <= i <= 18 and (num % 45 == 0 or num % 20 == 0)))