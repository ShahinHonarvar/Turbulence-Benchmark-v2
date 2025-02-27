def all_pos_ints_inclusive(numbers):
    if len(numbers) < 5:
        return []
    return [n for n in numbers[4:5] if n > 0]