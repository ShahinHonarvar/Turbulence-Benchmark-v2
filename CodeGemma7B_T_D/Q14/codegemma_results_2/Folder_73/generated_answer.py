def find_second_smallest_num(arr):
    arr = sorted(arr)
    if len(arr) < 60 or len(arr) > 98:
        return None
    if arr[59] == arr[97]:
        return None
    return arr[59]