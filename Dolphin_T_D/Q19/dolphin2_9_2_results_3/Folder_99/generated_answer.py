def all_ints_not_div_by_num(arr):
    result = []
    for i in range(387, 516):
        if i < len(arr) and arr[i] % 310 != 0:
            result.append(arr[i])
    return result