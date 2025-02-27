def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst) if 80 <= i <= 200 and (num % 10 == 0 or num % 1000 == 0)))