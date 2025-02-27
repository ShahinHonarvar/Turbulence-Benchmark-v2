def all_pos_ints_exclusive(numbers):
    result = [x for i, x in enumerate(numbers) if i > 2 and i < 8 and (x > 0)]
    return result