def sum_even_ints_inclusive(arr):
    if len(arr) < 30:
        return 0
    return sum((x for x in arr[29:94] if x % 2 == 0))