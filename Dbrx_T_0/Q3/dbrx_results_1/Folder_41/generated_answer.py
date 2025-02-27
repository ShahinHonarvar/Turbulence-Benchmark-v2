def all_pos_ints_inclusive(numbers):
    if len(numbers) < 13:
        return []
    return [n for n in numbers[6:12] if n > 0]