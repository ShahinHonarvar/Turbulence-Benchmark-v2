def find_second_smallest_num(arr):
    if not arr or len(arr) < 2:
        return None
    min_val = min(arr[0:9])
    arr.remove(min_val)
    if len(arr) == 1:
        return None
    second_min_val = min(arr[0:9])
    return second_min_val