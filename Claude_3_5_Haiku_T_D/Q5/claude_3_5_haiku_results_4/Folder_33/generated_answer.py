def all_neg_ints_inclusive(numbers):
    if len(numbers) <= 774:
        return []
    return [num for num in numbers[667:775] if num < 0]