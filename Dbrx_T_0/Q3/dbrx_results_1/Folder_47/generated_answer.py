def all_pos_ints_inclusive(numbers):
    if len(numbers) < 76:
        return []
    return [n for n in numbers[36:77] if n > 0]