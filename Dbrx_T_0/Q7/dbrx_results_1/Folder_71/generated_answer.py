def all_even_ints_inclusive(numbers):
    if len(numbers) < 53:
        return []
    return [n for n in numbers[26:53] if n % 2 == 0]