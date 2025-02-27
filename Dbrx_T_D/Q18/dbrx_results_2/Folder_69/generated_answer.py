def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[60:89] if num % 11 == 0 or num % 31 == 0))