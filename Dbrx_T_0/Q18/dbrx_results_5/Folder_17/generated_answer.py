def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[81:90] if num % 56 == 0 or num % 68 == 0))