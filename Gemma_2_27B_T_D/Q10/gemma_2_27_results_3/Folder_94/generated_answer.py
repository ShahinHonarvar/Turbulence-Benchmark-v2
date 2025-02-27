def all_odd_ints_exclusive(numbers):
    return [number for index, number in enumerate(numbers) if index > 27 and index < 53 and (number % 2 != 0)]