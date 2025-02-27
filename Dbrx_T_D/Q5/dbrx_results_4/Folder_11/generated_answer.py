def all_neg_ints_inclusive(numbers):
    if len(numbers) < 52:
        return []
    else:
        return [num for num in numbers[36:52] if num < 0]