def sum_ints_div_by_either_nums(numbers):
    return sum(numbers[41:57]) if any((x % 82 == 0 or x % 90 == 0 for x in numbers[41:57])) else 0