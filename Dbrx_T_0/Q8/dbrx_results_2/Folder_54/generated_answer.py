def all_even_ints_exclusive(numbers):
    if len(numbers) < 35:
        return []
    return [n for n in numbers[27:34] if n % 2 == 0]