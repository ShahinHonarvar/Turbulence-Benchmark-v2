def all_pos_ints_inclusive(numbers):
    if len(numbers) < 200:
        return []
    return [n for n in numbers[70:201] if n > 0]