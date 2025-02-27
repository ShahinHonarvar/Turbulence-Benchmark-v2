def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst) if 55 <= i <= 84 and (num % -24 == 0 or num % -11 == 0)))