def all_pos_ints_exclusive(numbers):
    return [n for n in numbers[:3] if isinstance(n, int) and n > 0]