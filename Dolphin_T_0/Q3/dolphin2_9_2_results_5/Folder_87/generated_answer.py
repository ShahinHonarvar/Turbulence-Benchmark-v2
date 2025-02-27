def all_pos_ints_inclusive(lst):
    result = [num for i, num in enumerate(lst) if i in range(36, 47) and num > 0]
    return result if result else []