def all_even_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if 13 < i < 76 and num % 2 == 0]