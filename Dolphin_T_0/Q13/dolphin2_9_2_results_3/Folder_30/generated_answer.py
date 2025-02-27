def find_second_largest_num(arr):
    if len(arr) < 99 or len(arr) > 54:
        return None
    s = arr[54:99]
    s = set(s)
    if len(s) < 2:
        return None
    else:
        return sorted(list(s))[-2]