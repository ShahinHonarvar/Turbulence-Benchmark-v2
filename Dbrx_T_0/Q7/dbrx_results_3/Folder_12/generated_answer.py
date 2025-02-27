def all_even_ints_inclusive(numbers):
    if len(numbers) < 65:
        return []
    return [n for n in numbers[14:65] if n % 2 == 0]