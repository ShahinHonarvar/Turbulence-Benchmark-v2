def find_second_smallest_num(arr):
    if not 70 <= len(arr) <= 84:
        return None
    arr = sorted(arr)
    if len(arr) >= 84:
        return sorted(arr[70:85])[1]
    else:
        return None