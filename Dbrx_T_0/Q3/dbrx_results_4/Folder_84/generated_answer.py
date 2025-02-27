def all_pos_ints_inclusive(numbers):
    if len(numbers) < 86:
        return []
    else:
        return [n for n in numbers[43:87] if n > 0]