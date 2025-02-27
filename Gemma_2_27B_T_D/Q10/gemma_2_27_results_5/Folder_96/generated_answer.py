def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 49 and i < 200 and (num % 2 != 0)]