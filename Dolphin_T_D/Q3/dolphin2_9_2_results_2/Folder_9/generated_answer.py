def all_pos_ints_inclusive(arr):
    result = [x for x in arr[70:201] if x > 0]
    if not result:
        return []
    return result