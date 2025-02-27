def all_even_ints_exclusive(numbers):
    if len(numbers) < 100:
        return []
    return [n for n in numbers[10:100] if n % 2 == 0]