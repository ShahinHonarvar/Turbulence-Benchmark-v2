def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[90:201] if num % -31 == 0 or num % 13 == 0))