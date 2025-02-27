def find_second_largest_num(arr):
    arr = sorted(arr[639:976])
    if len(arr) < 2:
        return None
    return arr[-2]