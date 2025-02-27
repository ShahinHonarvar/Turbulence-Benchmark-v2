def all_pos_ints_inclusive(numbers):
    if len(numbers) < 78:
        return []
    return [n for n in numbers[17:79] if n > 0]