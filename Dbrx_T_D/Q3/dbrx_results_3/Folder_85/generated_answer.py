def all_pos_ints_inclusive(numbers):
    if len(numbers) < 9:
        return []
    pos_ints = [n for n in numbers[5:9] if n > 0]
    return pos_ints