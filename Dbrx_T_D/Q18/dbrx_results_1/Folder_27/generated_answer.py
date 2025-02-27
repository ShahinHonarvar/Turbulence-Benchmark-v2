def sum_ints_div_by_either_nums(numbers):
    return sum((i for i in numbers[20:36] if i % -36 == 0 or i % -89 == 0))