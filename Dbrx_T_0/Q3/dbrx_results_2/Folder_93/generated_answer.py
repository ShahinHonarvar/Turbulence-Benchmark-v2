def all_pos_ints_inclusive(numbers):
    if len(numbers) < 95:
        return []
    return [n for n in numbers[74:95] if n > 0]