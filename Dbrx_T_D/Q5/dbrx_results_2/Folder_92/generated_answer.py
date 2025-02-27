def all_neg_ints_inclusive(numbers):
    if len(numbers) < 2:
        return []
    return [num for num in numbers[:2] if num < 0]