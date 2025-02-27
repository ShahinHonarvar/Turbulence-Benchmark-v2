def all_ints_div_by_both_two_nums(arr):
    result = []
    for i in range(18, 53):
        if arr[i] % 15 == 0 and arr[i] % 57 == 0:
            result.append(arr[i])
    return result