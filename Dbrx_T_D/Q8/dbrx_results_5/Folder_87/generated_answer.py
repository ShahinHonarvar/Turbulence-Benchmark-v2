def all_even_ints_exclusive(numbers):
    if len(numbers) < 99:
        return []
    return [n for n in numbers[32:99:2] if n % 2 == 0]