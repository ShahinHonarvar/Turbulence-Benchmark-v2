def all_pos_ints_inclusive(lst):
    if not any((True for _ in range(22, 64) if lst[_] > 0)):
        return []
    return [num for num in lst[22:63] if num > 0]