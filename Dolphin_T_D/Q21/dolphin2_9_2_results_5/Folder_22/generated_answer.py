def all_ints_div_by_num(arr):
    result = []
    for i in range(10, 11):
        if arr[i] % 1 == 0:
            result.append(arr[i])
    return result