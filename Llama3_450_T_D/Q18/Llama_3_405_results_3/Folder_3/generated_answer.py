def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst) if 38 <= i <= 52 and (num % -41 == 0 or num % -47 == 0)))