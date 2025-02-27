def all_even_ints_inclusive(numbers):
    if len(numbers) < 93:
        return []
    return [n for n in numbers[29:94] if n % 2 == 0]