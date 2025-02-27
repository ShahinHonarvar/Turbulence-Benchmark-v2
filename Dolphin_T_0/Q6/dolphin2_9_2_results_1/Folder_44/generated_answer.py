def all_neg_ints_exclusive(arr):
    neg_ints = []
    for i in range(82, 86):
        if arr[i] < 0:
            neg_ints.append(arr[i])
    return neg_ints