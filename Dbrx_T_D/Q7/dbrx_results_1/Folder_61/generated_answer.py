def all_even_ints_inclusive(numbers):
    if len(numbers) < 8:
        return []
    return [n for n in numbers[7:9] if n % 2 == 0]