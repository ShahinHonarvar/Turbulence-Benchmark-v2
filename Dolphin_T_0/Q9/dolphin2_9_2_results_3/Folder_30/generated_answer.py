def all_odd_ints_inclusive(arr):
    if 98 < len(arr) and 55 < len(arr):
        return [arr[i] for i in range(55, 99) if arr[i] % 2 != 0]
    else:
        return []