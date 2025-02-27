def sum_ints_div_by_either_nums(numbers):
    return sum((num for num in numbers[48:60] if num % 88 == 0 or num % 58 == 0)) if len(numbers) >= 60 else 0