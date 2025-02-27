def all_odd_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers) if i in range(91, 100) and num % 2 != 0]