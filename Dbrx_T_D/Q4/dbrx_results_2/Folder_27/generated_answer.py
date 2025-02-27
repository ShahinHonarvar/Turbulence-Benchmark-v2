def all_pos_ints_exclusive(numbers):
    if len(numbers) < 49:
        return []
    else:
        return [n for n in numbers[28:49] if n > 0]