def sum_ints_div_by_either_nums(numbers):
    return sum((x for i, x in enumerate(numbers[2:8]) if i % 7 == 0 or x % -7 == 0))