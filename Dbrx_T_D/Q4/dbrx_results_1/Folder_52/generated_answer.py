def all_pos_ints_exclusive(numbers):
    if len(numbers) < 95:
        return []
    else:
        return [n for n in numbers[93:94] if n > 0]