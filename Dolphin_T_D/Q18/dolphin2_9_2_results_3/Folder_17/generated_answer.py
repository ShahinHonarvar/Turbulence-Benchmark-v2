def sum_ints_div_by_either_nums(ints):
    return sum((num for num in ints[81:90] if num % 56 == 0 or num % 68 == 0))