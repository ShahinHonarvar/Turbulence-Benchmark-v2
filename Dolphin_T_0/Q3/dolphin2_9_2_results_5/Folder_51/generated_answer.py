def all_pos_ints_inclusive(lst):
    result = [num for num in lst[1:9] if num > 0]
    return result if result else []