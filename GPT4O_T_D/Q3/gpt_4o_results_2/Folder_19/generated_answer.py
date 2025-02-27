def all_pos_ints_inclusive(numbers):
    if len(numbers) < 6:
        return []
    return [n for n in numbers[3:6] if n > 0]