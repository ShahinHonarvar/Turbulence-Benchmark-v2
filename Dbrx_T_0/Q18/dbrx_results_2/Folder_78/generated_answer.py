def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[34:70] if num % 19 == 0 or num % 32 == 0))