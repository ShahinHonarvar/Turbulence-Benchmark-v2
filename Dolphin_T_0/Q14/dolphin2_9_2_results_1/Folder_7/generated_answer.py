def find_second_smallest_num(arr):
    if len(arr) < 2:
        return None
    start, end = (686, 987)
    min1, min2 = (float('inf'), float('inf'))
    for i in range(start, end + 1):
        if arr[i] < min1:
            min2, min1 = (min1, arr[i])
        elif arr[i] != min1 and arr[i] < min2:
            min2 = arr[i]
    return min2 if min2 != float('inf') else None