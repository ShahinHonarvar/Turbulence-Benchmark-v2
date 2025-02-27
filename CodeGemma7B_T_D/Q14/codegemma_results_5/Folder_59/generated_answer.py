def find_second_smallest_num(arr):
    if len(arr) < 2:
        return None
    arr.sort()
    return arr[1]