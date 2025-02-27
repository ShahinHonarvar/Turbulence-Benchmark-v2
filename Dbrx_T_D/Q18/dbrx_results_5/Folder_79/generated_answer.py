def sum_ints_div_by_either_nums(numbers):
    return sum((x for i, x in enumerate(numbers[8:10]) if x % -3 == 0 or x % 6 == 0))