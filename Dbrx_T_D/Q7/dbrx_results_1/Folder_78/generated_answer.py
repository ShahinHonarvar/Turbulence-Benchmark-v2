def all_even_ints_inclusive(numbers):
    if len(numbers) < 52 or len(numbers) < 43:
        return []
    return [num for num in numbers[43:52] if num % 2 == 0]