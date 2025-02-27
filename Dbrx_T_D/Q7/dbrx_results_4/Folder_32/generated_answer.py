def all_even_ints_inclusive(numbers):
    if len(numbers) < 97:
        return []
    else:
        return [n for n in numbers[21:98] if n % 2 == 0]