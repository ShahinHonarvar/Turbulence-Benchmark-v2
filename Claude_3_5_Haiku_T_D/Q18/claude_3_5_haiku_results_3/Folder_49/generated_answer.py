def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[80:201] if num % 10 == 0 or num % 1000 == 0))