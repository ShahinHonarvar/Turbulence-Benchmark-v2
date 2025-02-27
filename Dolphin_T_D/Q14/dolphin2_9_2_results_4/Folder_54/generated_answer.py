def find_second_smallest_num(arr):
    if len(arr) < 19:
        return None
    else:
        return sorted(arr[67:87])[1]