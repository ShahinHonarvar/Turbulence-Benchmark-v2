def all_pos_ints_exclusive(numbers):
    if len(numbers) < 93:
        return []
    return [n for n in numbers[59:93] if n > 0]