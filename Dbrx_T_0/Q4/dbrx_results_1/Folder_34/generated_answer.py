def all_pos_ints_exclusive(numbers):
    if len(numbers) < 200:
        return []
    return [n for n in numbers[60:200] if n > 0]