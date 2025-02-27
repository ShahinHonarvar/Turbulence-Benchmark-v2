def all_even_ints_inclusive(numbers):
    if len(numbers) < 35:
        return []
    return [n for n in numbers[31:35] if n % 2 == 0]