def all_even_ints_exclusive(numbers):
    if len(numbers) < 89:
        return []
    return [n for n in numbers[86:89] if n % 2 == 0]