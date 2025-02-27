def all_neg_ints_exclusive(numbers):
    if len(numbers) < 94:
        return []
    neg_ints = [num for num in numbers[93:94] if num < 0]
    return neg_ints