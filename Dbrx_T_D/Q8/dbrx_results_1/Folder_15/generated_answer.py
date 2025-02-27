def all_even_ints_exclusive(numbers):
    if len(numbers) < 4:
        return []
    return [n for n in numbers[:4] if n % 2 == 0]