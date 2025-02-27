def all_pos_ints_exclusive(numbers):
    if len(numbers) < 35:
        return []
    return [n for n in numbers[26:34] if n > 0]