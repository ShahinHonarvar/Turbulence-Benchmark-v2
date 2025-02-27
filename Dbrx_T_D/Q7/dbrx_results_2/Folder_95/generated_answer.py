def all_even_ints_inclusive(numbers):
    if len(numbers) < 83:
        return []
    return [n for n in numbers[82:87] if n % 2 == 0]