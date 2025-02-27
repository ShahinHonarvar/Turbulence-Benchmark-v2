def sum_ints_div_by_either_nums(numbers):
    return sum((x for x in numbers[1:5] if x % 4 == 0 or x % -6 == 0))