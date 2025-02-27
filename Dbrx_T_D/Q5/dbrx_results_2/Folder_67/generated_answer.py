def all_neg_ints_inclusive(numbers):
    if len(numbers) < 50:
        return []
    return [n for n in numbers[22:51] if n < 0]