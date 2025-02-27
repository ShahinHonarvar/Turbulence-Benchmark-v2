def all_neg_ints_exclusive(numbers):
    if len(numbers) >= 6:
        return [num for num in numbers[:6] if num < 0]
    else:
        return []