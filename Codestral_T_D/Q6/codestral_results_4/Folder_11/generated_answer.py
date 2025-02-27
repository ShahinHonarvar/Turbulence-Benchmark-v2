def all_neg_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 15 and i < 99 and (num < 0)]