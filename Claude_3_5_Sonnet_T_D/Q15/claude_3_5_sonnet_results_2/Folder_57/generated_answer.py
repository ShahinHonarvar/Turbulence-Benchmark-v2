def sum_odd_ints_inclusive(numbers):
    if len(numbers) < 56:
        return 0
    return sum((num for num in numbers[27:56] if num % 2 != 0))