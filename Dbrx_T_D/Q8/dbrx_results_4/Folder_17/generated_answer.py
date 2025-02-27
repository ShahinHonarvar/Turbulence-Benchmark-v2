def all_even_ints_exclusive(numbers):
    if len(numbers) < 97:
        return []
    return [n for n in numbers[62:96] if n % 2 == 0]