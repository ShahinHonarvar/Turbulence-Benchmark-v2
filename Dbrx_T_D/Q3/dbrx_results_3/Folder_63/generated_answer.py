def all_pos_ints_inclusive(numbers):
    if len(numbers) < 88:
        return []
    return [n for n in numbers[21:89] if n > 0]