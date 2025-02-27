def all_neg_ints_inclusive(numbers):
    if len(numbers) < 4:
        return []
    else:
        return [num for num in numbers[:5] if num < 0]