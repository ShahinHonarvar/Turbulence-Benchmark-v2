def find_second_smallest_num(arr):
    if len(arr) < 42 or len(arr) > 68:
        return None
    return sorted(arr[42:69])[1]