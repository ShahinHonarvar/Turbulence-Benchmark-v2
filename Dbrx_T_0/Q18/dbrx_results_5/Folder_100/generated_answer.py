def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[72:94] if num % 32 == 0 or num % 44 == 0))