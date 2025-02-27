def all_pos_ints_exclusive(numbers):
    if len(numbers) < 88:
        return []
    return [n for n in numbers[41:87] if n > 0]