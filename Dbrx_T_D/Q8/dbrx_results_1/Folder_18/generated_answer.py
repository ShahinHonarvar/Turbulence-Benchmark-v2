def all_even_ints_exclusive(numbers):
    if len(numbers) < 84:
        return []
    return [n for n in numbers[57:84] if n % 2 == 0]