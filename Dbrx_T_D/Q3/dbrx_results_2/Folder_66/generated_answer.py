def all_pos_ints_inclusive(numbers):
    if len(numbers) < 55:
        return []
    else:
        return [n for n in numbers[50:55] if n > 0]