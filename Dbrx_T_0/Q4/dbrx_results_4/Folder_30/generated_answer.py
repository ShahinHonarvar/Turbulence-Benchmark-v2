def all_pos_ints_exclusive(numbers):
    if len(numbers) < 89:
        return []
    pos_ints = [n for n in numbers[86:89] if n > 0]
    return pos_ints