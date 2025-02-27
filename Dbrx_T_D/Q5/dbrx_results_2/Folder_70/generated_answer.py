def all_neg_ints_inclusive(numbers):
    if len(numbers) < 33:
        return []
    return [num for num in numbers[28:33] if num < 0]