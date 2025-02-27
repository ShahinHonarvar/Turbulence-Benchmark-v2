def all_pos_ints_inclusive(lst):
    result = [INT for INT in lst[28:41] if INT > 0]
    if not result:
        result = []
    return result