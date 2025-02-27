def all_pos_ints_exclusive(numbers):
    if len(numbers) < 85:
        return []
    pos_ints = [n for n in numbers[72:84] if n > 0]
    return pos_ints