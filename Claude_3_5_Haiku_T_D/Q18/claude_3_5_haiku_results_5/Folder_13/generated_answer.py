def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[13:19] if num % 45 == 0 or num % 20 == 0))