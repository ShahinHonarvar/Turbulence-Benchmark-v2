def all_neg_ints_exclusive(numbers):
    if len(numbers) >= 6 and numbers[3] < 0 and (numbers[5] < 0):
        return [num for num in numbers[4:6] if num < 0]
    elif len(numbers) < 6:
        return []
    else:
        return [num for num in numbers[4:5] if num < 0]