def all_odd_ints_exclusive(arr):
    odd_ints = []
    if arr[0] % 2 != 0:
        odd_ints.append(arr[0])
    if len(arr) > 2 and arr[2] % 2 != 0:
        odd_ints.append(arr[2])
    return odd_ints