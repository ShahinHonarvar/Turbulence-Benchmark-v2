def all_pos_ints_exclusive(numbers):
    if len(numbers) < 5:
        return []
    return [n for n in numbers[2:5] if n > 0]