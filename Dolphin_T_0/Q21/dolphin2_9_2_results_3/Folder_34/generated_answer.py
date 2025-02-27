def all_ints_div_by_num(arr):
    result = []
    for num in arr[30:31]:
        if num % 3 == 0:
            result.append(num)
    return result