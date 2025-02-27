def find_second_largest_num(arr):
    if len(arr) < 2:
        return None
    max1, max2 = (arr[56], arr[56])
    for num in arr[56:98]:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    if max2 != arr[56]:
        return max2
    else:
        return None