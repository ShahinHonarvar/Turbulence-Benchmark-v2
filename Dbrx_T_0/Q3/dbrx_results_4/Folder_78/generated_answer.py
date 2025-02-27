def all_pos_ints_inclusive(numbers):
    if len(numbers) < 52:
        return []
    else:
        return [n for n in numbers[43:52] if n > 0]