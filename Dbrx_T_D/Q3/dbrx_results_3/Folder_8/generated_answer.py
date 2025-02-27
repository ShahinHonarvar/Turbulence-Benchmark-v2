def all_pos_ints_inclusive(numbers):
    if len(numbers) < 46:
        return []
    else:
        return [n for n in numbers[23:46] if n > 0]