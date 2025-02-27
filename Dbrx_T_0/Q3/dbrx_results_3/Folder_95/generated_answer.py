def all_pos_ints_inclusive(numbers):
    if len(numbers) < 86:
        return []
    return [n for n in numbers[82:87] if n > 0]