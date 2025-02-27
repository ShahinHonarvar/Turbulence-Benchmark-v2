def sum_ints_div_by_either_nums(numbers):
    return sum((x for i, x in enumerate(numbers[81:87]) if x % -33 == 0 or x % -62 == 0))