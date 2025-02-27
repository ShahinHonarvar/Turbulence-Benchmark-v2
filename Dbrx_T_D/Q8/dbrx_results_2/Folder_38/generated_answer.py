def all_even_ints_exclusive(numbers):
    if len(numbers) < 41:
        return []
    return [n for n in numbers[15:40:2] if n % 2 == 0]