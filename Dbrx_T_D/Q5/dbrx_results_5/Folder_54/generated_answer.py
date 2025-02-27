def all_neg_ints_inclusive(numbers):
    if len(numbers) < 55:
        return []
    return [n for n in numbers[34:56] if n < 0]