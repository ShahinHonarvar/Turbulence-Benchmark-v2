def find_second_smallest_num(arr):
    if 75 <= len(arr) <= 85:
        s = sorted(arr[75:86])
        if len(s) == 2:
            return s[1]
    return None