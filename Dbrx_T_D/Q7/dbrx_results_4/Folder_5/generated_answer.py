def all_even_ints_inclusive(numbers):
    if len(numbers) < 10:
        return []
    return [n for n in numbers[8:10] if n % 2 == 0]