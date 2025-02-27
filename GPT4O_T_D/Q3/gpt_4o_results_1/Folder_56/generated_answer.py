def all_pos_ints_inclusive(lst):
    if not lst or lst[0] <= 0:
        return []
    return [num for num in lst if 0 <= lst.index(num) <= 0 and num > 0]