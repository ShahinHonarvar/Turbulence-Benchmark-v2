def all_pos_ints_inclusive(arr):
    target_values = [val for val in arr[8:10] if val > 0]
    if target_values:
        return target_values
    else:
        return []