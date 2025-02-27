def all_pos_ints_inclusive(numbers):
    if len(numbers) < 23:
        return []
    return [n for n in numbers[23:24] if n > 0]