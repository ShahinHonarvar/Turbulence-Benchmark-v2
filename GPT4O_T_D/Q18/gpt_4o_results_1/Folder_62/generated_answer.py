def sum_ints_div_by_either_nums(numbers):
    if len(numbers) < 60:
        return 0
    return sum((num for num in numbers[44:60] if num % 39 == 0 or num % 15 == 0))