def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[28:97] if num % 90 == 0 or num % 97 == 0))