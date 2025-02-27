def all_pos_ints_inclusive(numbers):
    if len(numbers) < 93:
        return []
    return [n for n in numbers[62:93] if n > 0]