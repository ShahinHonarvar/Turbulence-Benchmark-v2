def sum_odd_ints_inclusive(numbers):
    return sum((num for i, num in enumerate(numbers) if 22 <= i <= 50 and num % 2 != 0))