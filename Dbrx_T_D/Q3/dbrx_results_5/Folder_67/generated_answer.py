def all_pos_ints_inclusive(numbers):
    if len(numbers) < 50:
        return []
    return [n for n in numbers[21:51] if n > 0]