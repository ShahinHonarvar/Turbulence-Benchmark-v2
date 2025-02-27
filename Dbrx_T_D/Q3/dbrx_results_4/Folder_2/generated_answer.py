def all_pos_ints_inclusive(numbers):
    if len(numbers) >= 40:
        return [n for n in numbers[14:40] if n > 0]
    else:
        return []