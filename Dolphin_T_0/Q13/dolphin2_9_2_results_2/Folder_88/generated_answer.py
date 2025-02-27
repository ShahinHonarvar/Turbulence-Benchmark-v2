def find_second_largest_num(arr):
    if len(arr) < 2 or len(arr) > 9 or arr[4] == arr[5] == arr[6] == arr[7] == arr[8]:
        return None
    max1 = max(arr[4:9])
    max_index1 = arr[4:9].index(max1) + 4
    del arr[max_index1]
    if len(arr) < 2:
        return None
    max2 = max(arr[4:9])
    return max2