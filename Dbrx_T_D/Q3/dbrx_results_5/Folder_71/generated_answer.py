def all_pos_ints_inclusive(numbers):
    if len(numbers) < 52:
        return []
    return [n for n in numbers[25:53] if n > 0]