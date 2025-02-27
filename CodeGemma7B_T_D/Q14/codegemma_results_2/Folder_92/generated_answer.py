def find_second_smallest_num(arr):
    arr.sort()
    if len(arr) < 2:
        return 'None'
    else:
        return arr[1]