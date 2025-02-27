def all_even_ints_exclusive(numbers):
    if len(numbers) < 8:
        return []
    return [n for n in numbers[2:7] if n % 2 == 0]