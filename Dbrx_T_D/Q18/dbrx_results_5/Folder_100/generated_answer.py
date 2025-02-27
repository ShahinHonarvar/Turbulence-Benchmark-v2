def sum_ints_div_by_either_nums(numbers):
    return sum((x for x in numbers[72:94] if x % 32 == 0 or x % 44 == 0))