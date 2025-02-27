def sum_ints_div_by_either_nums(numbers):
    return sum((x for i, x in enumerate(numbers[25:71]) if i % 74 == 0 or i % 15 == 0))