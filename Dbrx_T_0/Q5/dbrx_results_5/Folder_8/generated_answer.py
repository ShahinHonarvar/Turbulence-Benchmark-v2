def all_neg_ints_inclusive(numbers):
    if len(numbers) < 46:
        return []
    else:
        return [num for num in numbers[23:46] if num < 0]