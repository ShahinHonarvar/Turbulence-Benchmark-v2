def all_even_ints_inclusive(numbers):
    if len(numbers) < 86:
        return []
    return [n for n in numbers[75:86] if n % 2 == 0]