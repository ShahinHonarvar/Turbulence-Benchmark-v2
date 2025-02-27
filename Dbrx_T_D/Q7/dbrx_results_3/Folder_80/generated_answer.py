def all_even_ints_inclusive(numbers):
    if len(numbers) < 66:
        return []
    return [n for n in numbers[64:67] if n % 2 == 0]