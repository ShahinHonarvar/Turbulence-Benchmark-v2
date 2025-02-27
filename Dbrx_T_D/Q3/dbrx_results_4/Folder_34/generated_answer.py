def all_pos_ints_inclusive(numbers):
    if len(numbers) < 200 or len(numbers) < 60:
        return []
    else:
        return [n for n in numbers[60:201] if n > 0]