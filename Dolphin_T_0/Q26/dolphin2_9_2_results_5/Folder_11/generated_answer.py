def sum_in_range(arr):
    result = 0
    for num in arr:
        if num in range(11, 77):
            result += num
    return result