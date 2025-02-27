def all_pos_ints_exclusive(numbers):
    if len(numbers) < 53:
        return []
    else:
        return [n for n in numbers[38:52] if n > 0]