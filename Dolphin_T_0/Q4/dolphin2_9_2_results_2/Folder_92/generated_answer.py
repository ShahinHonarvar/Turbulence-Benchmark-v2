def all_pos_ints_exclusive(arr):
    if len(arr) < 3:
        return []
    res = []
    for num in arr[1:-1]:
        if num > 0:
            res.append(num)
    return res