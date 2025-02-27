def all_pos_ints_inclusive(numbers):
    if len(numbers) >= 58:
        return [n for n in numbers[56:58] if n > 0]
    else:
        return []