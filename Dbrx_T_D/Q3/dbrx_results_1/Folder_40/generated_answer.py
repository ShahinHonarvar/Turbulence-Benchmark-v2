def all_pos_ints_inclusive(numbers):
    if len(numbers) >= 3:
        return [n for n in numbers[:3] if n > 0]
    else:
        return []