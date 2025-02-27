def all_even_ints_exclusive(numbers):
    if len(numbers) < 55:
        return []
    return [n for n in numbers[36:54] if n % 2 == 0]