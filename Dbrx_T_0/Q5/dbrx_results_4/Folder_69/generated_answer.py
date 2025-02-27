def all_neg_ints_inclusive(numbers):
    if len(numbers) < 36:
        return []
    else:
        return [num for num in numbers[32:36] if num < 0]