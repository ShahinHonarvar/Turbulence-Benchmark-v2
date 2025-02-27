def all_even_ints_exclusive(numbers):
    if len(numbers) < 54:
        return []
    return [n for n in numbers[28:53:2] if n % 2 == 0]