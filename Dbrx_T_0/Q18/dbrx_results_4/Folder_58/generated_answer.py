def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[240:902] if num % 546 == 0 or num % 709 == 0))