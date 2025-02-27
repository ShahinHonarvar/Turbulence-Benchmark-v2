def sum_odd_ints_inclusive(numbers):
    if len(numbers) < 30:
        return 0
    return sum((num for num in numbers[29:94] if num % 2 != 0))