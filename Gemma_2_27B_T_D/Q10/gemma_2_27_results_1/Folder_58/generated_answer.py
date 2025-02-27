def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i >= 276 and i < 376 and (num % 2 != 0)]