def all_pos_ints_inclusive(numbers):
    if len(numbers) < 35:
        return []
    pos_ints = [n for n in numbers[32:36] if n > 0]
    return pos_ints