def sum_odd_ints_inclusive(arr):
    if len(arr) < 29:
        return 0
    return sum((x for x in arr[28:41] if x % 2 != 0))