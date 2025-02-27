def all_even_ints_exclusive(numbers):
    if len(numbers) < 85:
        return []
    return [n for n in numbers[55:84] if n % 2 == 0]