def all_even_ints_exclusive(numbers):
    return [number for i, number in enumerate(numbers) if number % 2 == 0 and 0 <= i < 10]