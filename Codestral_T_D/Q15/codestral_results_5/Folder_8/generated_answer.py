def sum_odd_ints_inclusive(numbers):
    return sum((num for num in numbers[23:24] if num % 2 != 0)) if 23 < len(numbers) else 0