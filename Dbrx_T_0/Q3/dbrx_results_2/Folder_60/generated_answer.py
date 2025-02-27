def all_pos_ints_inclusive(numbers):
    if len(numbers) < 86:
        return []
    return [n for n in numbers[74:86] if n > 0]