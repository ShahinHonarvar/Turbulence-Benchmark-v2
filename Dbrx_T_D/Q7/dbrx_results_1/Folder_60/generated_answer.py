def all_even_ints_inclusive(numbers):
    if len(numbers) < 85:
        return []
    return [n for n in numbers[74:86] if n % 2 == 0]