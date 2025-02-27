def all_pos_ints_exclusive(numbers):
    if len(numbers) < 86:
        return []
    return [n for n in numbers[35:85] if n > 0]