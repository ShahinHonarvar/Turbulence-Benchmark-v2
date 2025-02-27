def all_neg_ints_inclusive(numbers):
    if len(numbers) < 64 or len(numbers) >= 100:
        return []
    return [num for num in numbers[14:65] if num < 0]