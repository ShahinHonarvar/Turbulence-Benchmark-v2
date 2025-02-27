def find_n_th_smallest_num(arr):
    if len(arr) < 18 or len(arr) > 82:
        raise ValueError('List length must be between 18 and 82, inclusive.')
    arr.sort()
    return arr[17:83][5]