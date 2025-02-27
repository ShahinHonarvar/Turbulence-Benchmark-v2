def all_even_ints_exclusive(numbers):
    start = 276
    end = 376
    if len(numbers) < end:
        return []
    return [num for num in numbers[start:end:2] if num % 2 == 0]