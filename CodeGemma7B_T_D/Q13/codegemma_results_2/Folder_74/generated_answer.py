def find_second_largest_num(arr):
    arr = list(set(arr))
    if len(arr) <= 16:
        return 'None'
    arr.sort(reverse=True)
    if 16 < len(arr) <= 78:
        return arr[16]
    else:
        return 'None'