def all_neg_ints_exclusive(numbers):
    if len(numbers) < 70:
        return []
    return [n for n in numbers[13:70] if n < 0]