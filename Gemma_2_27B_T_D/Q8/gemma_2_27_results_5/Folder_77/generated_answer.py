def all_even_ints_exclusive(numbers):
    return [number for index, number in enumerate(numbers) if index > 110 and index < 473 and (number % 2 == 0)]