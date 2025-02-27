def all_pos_ints_inclusive(numbers):
    if len(numbers) < 2:
        return []
    return [n for n in numbers[:2] if n > 0]