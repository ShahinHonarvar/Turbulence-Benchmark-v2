def all_pos_ints_inclusive(numbers):
    if len(numbers) < 39:
        return []
    return [n for n in numbers[27:39] if n > 0]