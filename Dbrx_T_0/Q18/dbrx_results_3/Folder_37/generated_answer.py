def sum_ints_div_by_either_nums(numbers):
    return sum((x for x in numbers[2:8] if x % -1 == 0 or x % -7 == 0))