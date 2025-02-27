def all_even_ints_inclusive(numbers):
    if len(numbers) < 46:
        return []
    return [n for n in numbers[23:46] if n % 2 == 0]