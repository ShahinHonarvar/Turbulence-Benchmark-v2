def sum_ints_div_by_either_nums(numbers):
    return sum((x for i, x in enumerate(numbers[86:90]) if x % -61 == 0 or x % -79 == 0))