def all_even_ints_inclusive(numbers):
    if len(numbers) < 49:
        return []
    return [n for n in numbers[30:49] if n % 2 == 0]