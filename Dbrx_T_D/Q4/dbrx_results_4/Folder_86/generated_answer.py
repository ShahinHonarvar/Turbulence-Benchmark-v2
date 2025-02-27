def all_pos_ints_exclusive(numbers):
    if len(numbers) < 60:
        return []
    return [n for n in numbers[18:60] if n > 0]