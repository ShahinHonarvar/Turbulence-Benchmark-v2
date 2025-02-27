def all_neg_ints_exclusive(numbers):
    if len(numbers) < 4:
        return []
    return [num for num in numbers[:4] if num < 0]