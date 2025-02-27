def all_pos_ints_inclusive(lst):
    result = [val for val in lst[25:88] if val > 0]
    if not result:
        result = []
    return result