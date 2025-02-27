def all_even_ints_inclusive(numbers):
    if len(numbers) < 33:
        return []
    return [n for n in numbers[28:33] if n % 2 == 0]