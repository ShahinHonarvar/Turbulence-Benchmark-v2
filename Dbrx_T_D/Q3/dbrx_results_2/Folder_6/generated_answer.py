def all_pos_ints_inclusive(numbers):
    if len(numbers) < 67:
        return []
    else:
        return [n for n in numbers[10:67] if n > 0]