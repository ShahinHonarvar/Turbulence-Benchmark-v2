def all_odd_ints_inclusive(arr):
    ret = []
    for i in range(533, 606):
        if arr[i] % 2 != 0:
            ret.append(arr[i])
    return ret