def sum_even_ints_inclusive(numbers):
    return sum((num for i, num in enumerate(numbers) if 262 <= i <= 746 and num % 2 == 0))