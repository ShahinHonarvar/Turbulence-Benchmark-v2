def sum_ints_div_by_either_nums(numbers):
    return sum((x for x in numbers[20:36] if x % -36 == 0 or x % -89 == 0))