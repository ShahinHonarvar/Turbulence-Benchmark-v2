def all_even_ints_exclusive(numbers):
    if len(numbers) < 25:
        return []
    return [n for n in numbers[22:24] if n % 2 == 0]