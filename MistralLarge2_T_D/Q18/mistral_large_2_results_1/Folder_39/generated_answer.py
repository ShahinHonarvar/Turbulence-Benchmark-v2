def sum_ints_div_by_either_nums(ints):
    return sum((num for i, num in enumerate(ints) if 13 <= i <= 76 and (num % -66 == 0 or num % -32 == 0)))