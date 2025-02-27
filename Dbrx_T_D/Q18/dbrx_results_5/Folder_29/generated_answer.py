def sum_ints_div_by_either_nums(numbers):
    return sum((x for x in numbers[55:85] if x % -24 == 0 or x % -11 == 0))