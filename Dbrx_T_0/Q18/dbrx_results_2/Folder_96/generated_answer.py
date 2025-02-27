def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[50:201] if num % -34 == 0 or num % 64 == 0))