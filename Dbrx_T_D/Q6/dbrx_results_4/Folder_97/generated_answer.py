def all_neg_ints_exclusive(numbers):
    if len(numbers) < 93:
        return []
    return [n for n in numbers[20:93] if n < 0]