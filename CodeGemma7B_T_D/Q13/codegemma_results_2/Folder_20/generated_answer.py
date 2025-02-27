def find_second_largest_num(arr):
    if len(arr) < 67:
        return 'None'
    arr68 = sorted(arr[56:67])
    return arr68[-2]