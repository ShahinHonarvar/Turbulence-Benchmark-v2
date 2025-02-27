def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[35:65] if num % -30 == 0 or num % -95 == 0))