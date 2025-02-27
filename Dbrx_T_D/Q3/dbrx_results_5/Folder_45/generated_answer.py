def all_pos_ints_inclusive(numbers):
    if len(numbers) < 200:
        return []
    else:
        return [n for n in numbers[29:201] if n > 0]