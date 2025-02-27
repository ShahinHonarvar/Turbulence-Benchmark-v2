def all_even_ints_exclusive(numbers):
    if len(numbers) < 200:
        return []
    return [n for n in numbers[60:200:2] if n % 2 == 0]