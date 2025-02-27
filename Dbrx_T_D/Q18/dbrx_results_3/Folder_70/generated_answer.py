def sum_ints_div_by_either_nums(numbers):
    return sum((x for x in numbers[42:44] if x % 15 == 0 or x % 87 == 0))