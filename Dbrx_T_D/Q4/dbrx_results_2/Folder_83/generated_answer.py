def all_pos_ints_exclusive(numbers):
    if len(numbers) < 200:
        return []
    pos_ints = [n for n in numbers[90:200] if n > 0]
    return pos_ints