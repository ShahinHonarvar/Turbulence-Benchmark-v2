def all_odd_ints_inclusive(numbers):
    return [number for i, number in enumerate(numbers) if i >= 29 and i <= 93 and (number % 2 != 0)]