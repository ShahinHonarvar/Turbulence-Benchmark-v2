def all_pos_ints_exclusive(numbers):
    if len(numbers) < 3:
        return []
    return [n for n in numbers[1:3] if n > 0]