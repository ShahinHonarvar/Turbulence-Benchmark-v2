def all_pos_ints_exclusive(numbers):
    if len(numbers) < 41:
        return []
    else:
        return [n for n in numbers[15:41] if n > 0]