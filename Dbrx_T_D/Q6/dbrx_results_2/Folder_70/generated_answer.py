def all_neg_ints_exclusive(numbers):
    if len(numbers) < 82:
        return []
    else:
        return [num for num in numbers[38:81] if num < 0]