def all_ints_div_by_num(arr):
    result = []
    for i in range(10, 53, 1):
        if arr[i] % -12 == 0:
            result.append(arr[i])
    return result