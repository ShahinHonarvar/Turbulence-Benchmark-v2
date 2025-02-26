def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[61:89] if num % 31 == 0 or num % 11 == 0))