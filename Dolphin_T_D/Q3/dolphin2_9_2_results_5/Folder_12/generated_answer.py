def all_pos_ints_inclusive(list):
    result = [num for i, num in enumerate(list) if i >= 14 and i <= 64 and (num > 0)]
    return result if result else []