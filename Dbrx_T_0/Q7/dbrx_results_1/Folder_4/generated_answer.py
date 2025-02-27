def all_even_ints_inclusive(numbers):
    if len(numbers) < 93:
        return []
    return [n for n in numbers[12:93] if n % 2 == 0]