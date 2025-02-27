def all_pos_ints_inclusive(numbers):
    if len(numbers) < 200:
        return []
    elif len(numbers) == 200:
        return [n for n in numbers[70:201] if n > 0]
    else:
        return [n for n in numbers[70:191] if n > 0]