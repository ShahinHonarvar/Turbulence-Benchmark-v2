def all_pos_ints_exclusive(numbers):
    if len(numbers) < 91:
        return []
    return [n for n in numbers[44:91] if n > 0]