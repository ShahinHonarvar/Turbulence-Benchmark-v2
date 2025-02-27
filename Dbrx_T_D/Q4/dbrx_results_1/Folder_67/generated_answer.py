def all_pos_ints_exclusive(numbers):
    if len(numbers) >= 75:
        return [n for n in numbers[49:74] if n > 0]
    else:
        return []