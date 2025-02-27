def all_odd_ints_exclusive(numbers):
    return [number for i, number in enumerate(numbers) if i < 9 and i > 0 and (number % 2 != 0)]