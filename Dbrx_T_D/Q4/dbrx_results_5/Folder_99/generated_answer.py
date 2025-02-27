def all_pos_ints_exclusive(numbers):
    if len(numbers) < 573:
        return []
    pos_ints = [n for n in numbers[295:573] if n > 0]
    return pos_ints