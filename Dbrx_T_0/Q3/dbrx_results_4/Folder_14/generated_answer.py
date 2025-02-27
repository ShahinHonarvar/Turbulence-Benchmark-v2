def all_pos_ints_inclusive(numbers):
    if len(numbers) < 8:
        return []
    return [n for n in numbers[5:8] if n > 0]