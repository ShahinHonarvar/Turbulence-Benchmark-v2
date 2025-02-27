def all_even_ints_inclusive(numbers):
    if len(numbers) < 55:
        return []
    return [n for n in numbers[50:55] if n % 2 == 0]