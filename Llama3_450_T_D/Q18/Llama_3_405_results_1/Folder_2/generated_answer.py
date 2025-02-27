def sum_ints_div_by_either_nums(lst):
    return sum((num for i, num in enumerate(lst) if 73 <= i <= 86 and (num % 54 == 0 or num % 82 == 0)))