def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[30:201] if num % -115 == 0 or num % 115 == 0))