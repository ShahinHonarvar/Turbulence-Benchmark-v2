def all_ints_div_by_num(arr):
    result = []
    for i in arr[5:9]:
        if i % -9 == 0:
            result.append(i)
    return result