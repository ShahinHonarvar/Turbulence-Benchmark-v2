def all_even_ints_inclusive(numbers):
    if len(numbers) < 55:
        return []
    return [n for n in numbers[27:56] if n % 2 == 0]