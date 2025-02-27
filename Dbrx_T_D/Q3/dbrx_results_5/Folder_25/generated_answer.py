def all_pos_ints_inclusive(numbers):
    if len(numbers) < 93:
        return []
    pos_ints = [n for n in numbers[29:94] if n > 0]
    return pos_ints