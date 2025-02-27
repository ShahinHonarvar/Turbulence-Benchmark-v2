def all_even_ints_exclusive(numbers):
    return [number for i, number in enumerate(numbers) if i >= 80 and i < 200 and (number % 2 == 0)]