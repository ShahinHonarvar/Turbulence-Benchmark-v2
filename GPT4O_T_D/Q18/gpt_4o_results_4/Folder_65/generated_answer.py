def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[50:93] if num % -94 == 0 or num % -95 == 0))