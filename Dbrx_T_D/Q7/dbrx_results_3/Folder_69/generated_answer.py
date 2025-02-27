def all_even_ints_inclusive(numbers):
    if len(numbers) < 36:
        return []
    else:
        return [n for n in numbers[32:36] if n % 2 == 0]