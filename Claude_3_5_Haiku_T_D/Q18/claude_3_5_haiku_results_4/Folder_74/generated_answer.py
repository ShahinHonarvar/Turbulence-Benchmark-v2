def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[90:98] if num % 13 == 0 or num % 35 == 0))