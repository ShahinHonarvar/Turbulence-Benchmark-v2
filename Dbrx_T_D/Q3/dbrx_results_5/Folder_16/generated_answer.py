def all_pos_ints_inclusive(numbers):
    if len(numbers) < 37:
        return []
    return [n for n in numbers[33:37] if n > 0]