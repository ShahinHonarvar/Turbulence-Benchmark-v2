def all_neg_ints_inclusive(numbers):
    if len(numbers) < 5:
        return []
    return [num for num in numbers[3:6] if num < 0]