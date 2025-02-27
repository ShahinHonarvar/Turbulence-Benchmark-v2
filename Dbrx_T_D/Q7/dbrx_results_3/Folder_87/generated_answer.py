def all_even_ints_inclusive(numbers):
    if len(numbers) < 47:
        return []
    return [n for n in numbers[36:47] if n % 2 == 0]