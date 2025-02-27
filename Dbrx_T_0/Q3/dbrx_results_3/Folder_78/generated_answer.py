def all_pos_ints_inclusive(numbers):
    if len(numbers) < 52 or len(numbers) < 43:
        return []
    else:
        return [n for n in numbers[43:52] if n > 0]