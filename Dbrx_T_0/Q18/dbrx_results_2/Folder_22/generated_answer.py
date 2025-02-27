def sum_ints_div_by_either_nums(numbers):
    return sum((x for x in numbers[40:201] if x % 21 == 0 or x % 71 == 0))