def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[20:201] if num % -20 == 0 or num % -200 == 0))