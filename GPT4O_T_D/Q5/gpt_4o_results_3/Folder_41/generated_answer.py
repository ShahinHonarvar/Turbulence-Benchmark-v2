def all_neg_ints_inclusive(numbers):
    if len(numbers) < 7:
        return []
    return [num for num in numbers[6:7] if num < 0]