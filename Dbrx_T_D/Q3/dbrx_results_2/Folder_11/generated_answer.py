def all_pos_ints_inclusive(numbers):
    if len(numbers) < 52:
        return []
    else:
        return [num for num in numbers[37:52] if num > 0]