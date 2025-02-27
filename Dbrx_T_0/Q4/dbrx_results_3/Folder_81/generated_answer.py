def all_pos_ints_exclusive(numbers):
    if len(numbers) < 100:
        return []
    return [n for n in numbers[10:100] if n > 0]