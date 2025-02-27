def all_even_ints_exclusive(numbers):
    if len(numbers) < 10:
        return []
    return [n for n in numbers[6:9] if n % 2 == 0]