def find_second_largest_num(arr):
    if len(arr) < 60:
        return 'None'
    arr.sort(reverse=True)
    return arr[50:55][-2]