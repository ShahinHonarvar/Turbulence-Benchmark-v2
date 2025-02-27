def all_pos_ints_inclusive(numbers):
    if len(numbers) < 65:
        return []
    else:
        return [n for n in numbers[14:65] if n > 0]