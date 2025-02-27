def all_pos_ints_exclusive(numbers):
    if len(numbers) < 8:
        return []
    else:
        return [n for n in numbers[2:8] if n > 0]