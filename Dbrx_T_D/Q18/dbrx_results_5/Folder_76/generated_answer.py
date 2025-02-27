def sum_ints_div_by_either_nums(numbers):
    return sum((num for i, num in enumerate(numbers[250:630]) if i % 850 == 0 or i % 587 == 0))