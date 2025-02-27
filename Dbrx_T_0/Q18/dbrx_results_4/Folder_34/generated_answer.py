def sum_ints_div_by_either_nums(numbers):
    return sum((x for x in numbers[60:201] if x % 9 == 0 or x % 11 == 0))