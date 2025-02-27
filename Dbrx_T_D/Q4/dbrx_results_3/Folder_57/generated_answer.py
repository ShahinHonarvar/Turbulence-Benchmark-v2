def all_pos_ints_exclusive(numbers):
    if len(numbers) < 37:
        return []
    return [n for n in numbers[18:37] if n > 0]