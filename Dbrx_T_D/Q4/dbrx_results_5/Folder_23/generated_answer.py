def all_pos_ints_exclusive(numbers):
    if len(numbers) < 53:
        return []
    return [n for n in numbers[29:53] if n > 0]