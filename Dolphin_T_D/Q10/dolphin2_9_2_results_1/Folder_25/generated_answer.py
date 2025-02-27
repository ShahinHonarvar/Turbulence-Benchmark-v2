def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if 41 < i < 69 and num % 2 != 0]