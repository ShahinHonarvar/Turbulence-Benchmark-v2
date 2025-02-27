def all_odd_ints_exclusive(arr):
    if len(arr) < 8:
        return []
    else:
        odd_ints = [i for i in arr[2:8] if i % 2 != 0]
        return odd_ints