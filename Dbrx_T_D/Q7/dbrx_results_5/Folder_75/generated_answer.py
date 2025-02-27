def all_even_ints_inclusive(numbers):
    if len(numbers) < 58:
        return []
    else:
        return [n for n in numbers[56:58] if n % 2 == 0]