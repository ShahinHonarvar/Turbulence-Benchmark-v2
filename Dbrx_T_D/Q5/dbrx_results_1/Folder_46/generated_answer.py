def all_neg_ints_inclusive(arr):
    if len(arr) < 87:
        return []
    return [i for i in arr[30:88] if i < 0]