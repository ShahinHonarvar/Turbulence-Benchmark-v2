def sum_ints_div_by_either_nums(numbers):
    if len(numbers) < 85:
        return 0
    return sum((num for num in numbers[55:85] if num % -24 == 0 or num % -11 == 0))