def all_even_ints_exclusive(numbers):
    if len(numbers) < 75:
        return []
    return [n for n in numbers[49:75:2] if n % 2 == 0]