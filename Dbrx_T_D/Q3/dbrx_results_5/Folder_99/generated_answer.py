def all_pos_ints_inclusive(numbers):
    if len(numbers) < 370:
        return []
    return [n for n in numbers[310:371] if n > 0]