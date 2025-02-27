def all_neg_ints_exclusive(numbers):
    if len(numbers) >= 89:
        start, end = (86, 89)
        return [num for num in numbers[start:end] if num < 0]
    else:
        return []