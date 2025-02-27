def all_pos_ints_inclusive(numbers):
    if len(numbers) >= 52:
        return [num for num in numbers[43:52] if num > 0]
    else:
        return []