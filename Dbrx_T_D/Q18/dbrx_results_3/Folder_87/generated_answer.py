def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[18:53] if num % 15 == 0 or num % 57 == 0))