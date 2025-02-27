def all_pos_ints_inclusive(lst):
    result = [num for num in lst[:9] if num > 0]
    if not result:
        result = []
    return result