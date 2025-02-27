def all_even_ints_inclusive(numbers):
    if len(numbers) < 69:
        return []
    return [n for n in numbers[42:69] if n % 2 == 0]