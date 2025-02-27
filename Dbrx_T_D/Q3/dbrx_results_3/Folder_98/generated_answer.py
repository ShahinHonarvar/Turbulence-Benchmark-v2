def all_pos_ints_inclusive(numbers):
    if len(numbers) < 7:
        return []
    else:
        return [n for n in numbers[:7] if n > 0]