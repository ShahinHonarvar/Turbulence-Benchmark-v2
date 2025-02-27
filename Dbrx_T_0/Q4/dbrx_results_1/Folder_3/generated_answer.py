def all_pos_ints_exclusive(numbers):
    if len(numbers) < 93:
        return []
    return [n for n in numbers[78:93] if n > 0]