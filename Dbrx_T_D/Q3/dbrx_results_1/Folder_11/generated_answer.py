def all_pos_ints_inclusive(numbers):
    if len(numbers) >= 52:
        return [n for n in numbers[36:52] if n > 0]
    else:
        return []