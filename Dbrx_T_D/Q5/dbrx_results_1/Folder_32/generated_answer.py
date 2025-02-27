def all_neg_ints_inclusive(numbers):
    if len(numbers) < 97:
        return []
    return [n for n in numbers[21:98] if n < 0]