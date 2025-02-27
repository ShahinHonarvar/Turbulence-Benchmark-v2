def all_pos_ints_inclusive(numbers):
    if len(numbers) < 36:
        return []
    return [n for n in numbers[32:36] if n > 0]