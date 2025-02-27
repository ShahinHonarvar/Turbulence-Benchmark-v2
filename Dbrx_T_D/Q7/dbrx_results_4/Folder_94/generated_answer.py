def all_even_ints_inclusive(numbers):
    if len(numbers) < 41:
        return []
    result = [n for n in numbers[28:41] if n % 2 == 0]
    return result