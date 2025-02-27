def all_pos_ints_exclusive(numbers):
    return [x for i, x in enumerate(numbers) if 0 < i < 10 and x > 0]