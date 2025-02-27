def all_even_ints_exclusive(numbers):
    result = [num for i, num in enumerate(numbers) if 30 < i < 200 and num % 2 == 0]
    return result if result else []