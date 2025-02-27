def sum_ints_div_by_either_nums(numbers):
    return sum((x for x in numbers[30:201] if x % -115 == 0 or x % 115 == 0))