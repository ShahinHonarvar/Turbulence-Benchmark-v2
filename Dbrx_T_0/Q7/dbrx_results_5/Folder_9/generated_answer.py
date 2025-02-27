def all_even_ints_inclusive(numbers):
    if len(numbers) < 73:
        return []
    return [n for n in numbers[73] if n % 2 == 0]