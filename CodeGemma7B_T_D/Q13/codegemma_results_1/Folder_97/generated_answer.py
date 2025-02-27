def find_second_largest_num(arr):
    try:
        arr.sort(reverse=True)
        return arr[40:81][1]
    except IndexError:
        return 'None'