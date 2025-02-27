def all_pos_ints_exclusive(numbers):
    if len(numbers) >= 6:
        return [n for n in numbers[4:6] if n > 0]
    else:
        return []