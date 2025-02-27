def all_pos_ints_exclusive(numbers):
    if len(numbers) < 85:
        return []
    return [n for n in numbers[36:85] if n > 0]