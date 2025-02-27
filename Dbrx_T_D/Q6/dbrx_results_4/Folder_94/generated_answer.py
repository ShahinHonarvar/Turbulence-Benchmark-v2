def all_neg_ints_exclusive(numbers):
    if len(numbers) < 54 or len(numbers) < 28:
        return []
    return [n for n in numbers[28:53] if n < 0]