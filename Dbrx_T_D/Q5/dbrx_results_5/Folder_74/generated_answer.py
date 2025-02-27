def all_neg_ints_inclusive(numbers):
    if len(numbers) < 78:
        return []
    return [num for num in numbers[17:79] if num < 0]