def all_even_ints_inclusive(numbers):
    if len(numbers) < 8:
        return []
    return [n for n in numbers[6:8] if n % 2 == 0]