def all_even_ints_inclusive(numbers):
    if len(numbers) < 39:
        return []
    return [n for n in numbers[28:39] if n % 2 == 0]