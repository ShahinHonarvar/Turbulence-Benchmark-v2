def all_even_ints_exclusive(numbers):
    if len(numbers) < 93:
        return []
    return [n for n in numbers[59:93] if n % 2 == 0]