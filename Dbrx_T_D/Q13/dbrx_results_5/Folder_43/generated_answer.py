def find_second_largest_num(arr):
    if len(arr) < 2 or len(arr[68:87]) < 2:
        return None
    max1 = max(arr[68:87])
    second_max = max1
    for num in arr[68:87]:
        if num < max1:
            second_max = max(second_max, num)
    return second_max if second_max < max1 else None