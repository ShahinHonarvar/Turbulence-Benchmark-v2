def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[200:202] if num % 17 == 0 or num % -5 == 0))