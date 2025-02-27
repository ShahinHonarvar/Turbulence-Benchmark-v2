def all_pos_ints_inclusive(numbers):
    if len(numbers) < 89:
        return []
    return [n for n in numbers[74:89] if n > 0]