def all_even_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if 20 < i < 200 and num % 2 == 0]