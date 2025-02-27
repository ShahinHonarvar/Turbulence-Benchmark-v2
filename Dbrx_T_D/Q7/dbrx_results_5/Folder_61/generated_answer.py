def all_even_ints_inclusive(numbers):
    if len(numbers) < 14:
        return []
    return [n for n in numbers[7:10] if n % 2 == 0]