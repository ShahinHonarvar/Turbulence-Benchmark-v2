def all_even_ints_exclusive(numbers):
    if len(numbers) <= 43:
        return []
    return [num for num in numbers[43:87] if num % 2 == 0]