def all_pos_ints_exclusive(numbers):
    if len(numbers) < 13:
        return []
    return [n for n in numbers[12:70] if n > 0]