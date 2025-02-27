def all_neg_ints_inclusive(numbers):
    if len(numbers) < 60:
        return []
    return [n for n in numbers[25:60] if n < 0]