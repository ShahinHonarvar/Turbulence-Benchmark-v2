def all_pos_ints_inclusive(arr):
    if len(arr) < 750:
        return []
    else:
        return [i for i in arr[246:751] if i > 0]