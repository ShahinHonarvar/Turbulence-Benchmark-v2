def all_pos_ints_exclusive(numbers):
    if len(numbers) < 86:
        return []
    return [n for n in numbers[81:86] if n > 0]