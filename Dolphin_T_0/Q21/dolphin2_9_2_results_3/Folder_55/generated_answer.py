def all_ints_div_by_num(arr):
    res = []
    for i in range(2):
        if arr[i] % 2 == 0:
            res.append(arr[i])
    return res