def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst) if 60 <= i <= 200 and (num % 9 == 0 or num % 11 == 0)))