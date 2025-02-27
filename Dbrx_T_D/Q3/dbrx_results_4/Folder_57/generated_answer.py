def all_pos_ints_inclusive(numbers):
    if len(numbers) < 55:
        return []
    else:
        return [n for n in numbers[26:56] if n > 0]