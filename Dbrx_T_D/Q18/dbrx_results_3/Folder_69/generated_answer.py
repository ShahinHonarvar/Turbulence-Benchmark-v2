def sum_ints_div_by_either_nums(numbers):
    return sum((x for x in numbers[60:89] if x % 31 == 0 or x % 11 == 0))