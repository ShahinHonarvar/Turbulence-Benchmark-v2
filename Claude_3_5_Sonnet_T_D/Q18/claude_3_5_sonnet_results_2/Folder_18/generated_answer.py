def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[55:67] if num % 22 == 0 or num % 82 == 0))