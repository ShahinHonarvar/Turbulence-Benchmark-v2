def all_pos_ints_inclusive(integers):
    if len(integers) <= 82:
        return []
    result = [num for num in integers[56:83] if num > 0]
    return result