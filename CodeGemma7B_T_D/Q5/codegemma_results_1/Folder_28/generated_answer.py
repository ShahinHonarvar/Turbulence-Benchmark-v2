def all_neg_ints_inclusive(arr):
    temp = []
    for i in range(62, 64):
        if arr[i] < 0:
            temp.append(arr[i])
    return temp or []